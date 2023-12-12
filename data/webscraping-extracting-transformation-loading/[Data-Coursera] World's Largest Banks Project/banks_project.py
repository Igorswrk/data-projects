# Code for ETL operations on Country-GDP data


import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime
import sqlite3
import numpy as np

# Exchange rate CSV path = https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMSkillsNetwork-PY0221EN-Coursera/labs/v2/exchange_rate.csv

def log_progress(message):
    ''' This function logs the mentioned message of a given stage of the
    code execution to a log file. Function returns nothing'''

    timestamp_format = '%Y-%h-%d-%H:%M:%S' # Year-Monthname-Day-Hour-Minute-Second
    now = datetime.now()
    timestamp = now.strftime(timestamp_format)
    with open("./out/code_log.txt", "a") as log:
        log.write(timestamp+' : '+message + '\n')


def extract(url, table_attribs):
    ''' This function aims to extract the required information from the website and save it to a data frame.
    The function returns the data frame for further processing.'''

    web_page = requests.get(url).text
    soup = BeautifulSoup(web_page, 'html.parser')

    table = soup.find_all(
        'table',
        attrs={"class" : "wikitable sortable mw-collapsible"}
    )[0].find('tbody')

    rows = table.find_all('tr')

    df = pd.DataFrame(columns=table_attribs)

    for count, row in enumerate(rows, start=1):
        if (count > 1):
            name = row.find_all('td')[1].text.replace("\n", '').replace(' ', '', 1)
            mc_usd_billion = float(row.find_all('td')[2].text)

            dict = {
                "Name" : [name],
                "MC_USD_Billion" : [mc_usd_billion]
            }

            df_aux = pd.DataFrame(dict)
            df = pd.concat([df, df_aux], ignore_index=True)

    return df


def transform(df, csv_path):
    ''' This function accesses the CSV file for exchange rate
    information, and adds three columns to the data frame, each
    containing the transformed version of Market Cap column to
    respective currencies'''

    # file exchange rate
    df_exchange_rate = pd.read_csv(csv_path, index_col='Currency')
    
    rate_eur = df_exchange_rate.loc['EUR', 'Rate']
    rate_gbp = df_exchange_rate.loc['GBP', 'Rate']
    rate_inr = df_exchange_rate.loc['INR', 'Rate']

    # Adding new columns required
    exchange_rate ={
        'EUR' : rate_eur,
        'GBP' : rate_gbp,
        'INR' : rate_inr
    }

    df['MC_GBP_Billion'] = [np.round(x*exchange_rate['GBP'], 2) for x in df['MC_USD_Billion']]
    df['MC_EUR_Billion'] = [np.round(x*exchange_rate['EUR'], 2) for x in df['MC_USD_Billion']]
    df['MC_INR_Billion'] = [np.round(x*exchange_rate['INR'], 2) for x in df['MC_USD_Billion']]
    
    return df

def load_to_csv(df, output_path):
    ''' This function saves the final data frame as a CSV file in
    the provided path. Function returns nothing.'''

    df.to_csv(output_path)

def load_to_db(df, sql_connection, table_name):
    ''' This function saves the final data frame to a database
    table with the provided name. Function returns nothing.'''

    df.to_sql(table_name, sql_connection, if_exists='replace', index=False)

    
def run_query(query_statement, sql_connection):
    ''' This function runs the query on the database table and
    prints the output on the terminal. Function returns nothing. '''

    print(pd.read_sql(query_statement, sql_connection))


''' Here, you define the required entities and call the relevant
functions in the correct order to complete the project. Note that this
portion is not inside any function.'''

URL = "https://web.archive.org/web/20230908091635/https://en.wikipedia.org/wiki/List_of_largest_banks"
table_attrs_extract = ["Name", "MC_USD_Billion"]
csv_path_out = "./out/Largest_banks_data.csv"
db_name = "./out/Banks.db"
table_name = "Largest_banks"
csv_path_exchange = "./input/exchange_rate.csv"

log_progress("Preliminaries complete. Initiating ETL process")

df = extract(URL, table_attrs_extract)
log_progress("Data extraction complete. Initiating Transformation process")

df = transform(df, csv_path_exchange)
log_progress("Data transformation complete. Initiating Loading process")

load_to_csv(df, csv_path_out)
log_progress("Data saved to CSV file")

conn = sqlite3.connect(db_name)
log_progress("SQL Connection initiated")

load_to_db(df, conn, table_name)
log_progress("Data loaded to Database as a table, Executing queries")

print("SELECT * FROM Largest_banks")
run_query("SELECT * FROM Largest_banks", conn)

print("\nSELECT AVG(MC_GBP_Billion) FROM Largest_banks")
run_query("SELECT AVG(MC_GBP_Billion) FROM Largest_banks", conn)

print("\nSELECT Name from Largest_banks LIMIT 5")
run_query("SELECT Name from Largest_banks LIMIT 5", conn)

log_progress("Process Complete")

conn.close()
log_progress("Server Connection closed")
