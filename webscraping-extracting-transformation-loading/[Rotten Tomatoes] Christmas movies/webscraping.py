from bs4 import BeautifulSoup
import pandas as pd
import requests
import matplotlib.pyplot as plt

url = 'https://editorial.rottentomatoes.com/guide/best-christmas-movies/'
csv_path = './out/thebestmovies.csv'

html_page = requests.get(url).text
soup = BeautifulSoup(html_page, 'html.parser')

body = soup.find("body", attrs={"class" : "body"})
items = soup.find_all("div", attrs={"class" : "row countdown-item"})

df = pd.DataFrame(columns=["Place", "Movie Title", "Start Year", "Tomatometer Score", "Directed By"])

for item in items:
    movies_index = item.find_all(
        "div",
        attrs={"class" : "countdown-index-resposive"}
    )

    movies_informations = item.find_all(
        "div",
        attrs={"class" : "article_movie_title"}
    )

    movies_details = item.find_all(
        "div",
        attrs={"class" : "countdown-item-details"}
    )

    index = int(movies_index[0].text.split('#')[1])

    title = movies_informations[0].h2.find(
        "a",
        href=True
    ).text

    year = int(movies_informations[0].h2.find(
        "span",
        attrs={"class" : "start-year"}
    ).text[1:5])

    tomatometer_score = float(movies_informations[0].h2.find(
        "span",
        attrs={"class" : "tMeterScore"}
    ).text.split('%')[0]) / 100.0

    director = movies_details[0].find(
        "div",
        attrs={"class" : "director"}
    ).a.text

    dict = {
        "Place" : [index],
        "Movie Title" : [title],
        "Start Year" : [year],
        "Tomatometer Score" : [tomatometer_score],
        "Directed By" : [director]
    }

    df1 = pd.DataFrame(dict)
    df = pd.concat([df, df1], ignore_index=True)

df.to_csv(csv_path)


