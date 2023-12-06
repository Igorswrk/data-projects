import pandas as pd
import requests
from bs4 import BeautifulSoup
from datetime import datetime
import sqlite3
import time

# known variables

json_name = "./out/Countries_by_GDP.json"
table_name = "Countries_by_GDP"
db_name = "./out/World_Economies.db"
table_columns = ['Country', 'GDP_USD_billion']
file_log_name = "./out/etl_project_log.txt"
URL = "https://web.archive.org/web/20230902185326/https://en.wikipedia.org/wiki/List_of_countries_by_GDP_%28nominal%29"

def extract_table(url, attrs, mode, tag):
    web_page = requests.get(URL).text
    soup = BeautifulSoup(web_page, mode)
    return soup.find_all(tag, attrs=attrs)

def transform(df, rows):
    for count, row in enumerate(rows):
        if count > 3:
            column = row.find_all('td')
            country = column[0].text
            gdp_usd_billion = float(column[2].text.replace(',', '').replace('—', '0'))
            gdp_usd_billion = round(gdp_usd_billion / 1000, 2) # Billion

            dict = {
                'Country' : [country],
                'GDP_USD_billion' : [gdp_usd_billion]
            }

            df_aux = pd.DataFrame(dict)
            df = pd.concat([df, df_aux], ignore_index=True)

    return df

# load to json
def load_json(json_name):
    df.to_json(json_name)

def create_db(db_name):
    return sqlite3.connect(db_name)

def create_table(table_name, conn):
    df.to_sql(table_name, conn, if_exists='replace', index=False)

def query_db(query_statement):
    return pd.read_sql(query_statement, conn)

def close_db(conn):
    conn.close()

def log(message):
    timestamp_format = '%Y-%h-%d-%H:%M:%S' # Year-Monthname-Day-Hour-Minute-Second
    now = datetime.now()
    timestamp = now.strftime(timestamp_format)
    with open(file_log_name, "a") as log:
        log.write(timestamp + ',' + message + '\n')


while True:
    log("starting data extract")

    log("extract table of countries by GDP")
    table = extract_table(
        URL,
        {'class': 'wikitable sortable static-row-numbers plainrowheaders srn-white-background'},
        'html.parser',
        'table'
    )[0].find_all('tbody')

    rows = table[0].find_all('tr')

    df = pd.DataFrame(columns=table_columns)

    log("transform data")
    df = transform(df, rows)

    log("loading data into json")
    load_json(json_name)

    log(f"creating database {db_name}")
    conn = create_db(db_name)

    log(f"creating table {table_name}")
    create_table(table_name, conn)

    log("returning countries required")
    query = f"SELECT * FROM {table_name} WHERE GDP_USD_billion >= 100.00"
    print(query)
    print("\n---")
    query_output = query_db(query)
    print(query_output)

    close_db(conn)
    log("Done!\n")
    time.sleep(30)