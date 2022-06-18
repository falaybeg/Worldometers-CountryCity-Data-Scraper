import pandas as pd
import requests
import numpy as np
from bs4 import BeautifulSoup
from country_data import *


header_data = ["city_id", "City_Name", "Population", "country_id"]
country_df = get_country_data()

def scrapping_city_data(country_df):
    url2 = "https://www.worldometers.info/world-population/population-by-country/"
    page = requests.get(url2)
    soup = BeautifulSoup(page.content, "html.parser")
    table = soup.find('table')
    table_body = table.find('tbody')
    country_link = []

    for a in table_body.find_all('a', href=True):
        country_link.append(a.get("href"))
    
    number = 1
    city_data = []
    country_id = int(country_df[['country_id']].values[0])

    for i in country_link:
        website = "https://www.worldometers.info"
        page = requests.get(website+i)
        pop_city = BeautifulSoup(page.content, "html.parser")
            
        table_cities = pop_city.find('table' ,attrs={'class':'table table-hover table-condensed table-list'})

        if(table_cities is not None):
            for row in table_cities.select('tbody tr'):
                city_text = [country_id, [a.text for a in row.find_all('td')]]
                city_data.append(city_text)
                #print(city_text)       
            country_id += 1
        else:
            print("NoneType deger var")

    return pd.DataFrame(city_data, columns=["country_id", "values"])


def get_city_data(country_df):
    city_df_v1 = scrapping_city_data(country_df)
    city_df = city_df_v1["values"].apply(pd.Series)
    #city_df.columns = header_data
    city_df["country_id"] = city_df_v1["country_id"]
    city_df.columns = header_data
    city_df["Population"] = city_df['Population'].replace(',','', regex=True)
    city_df['city_id'] = city_df['city_id'].astype('int')
    city_df['Population'] = city_df['Population'].astype('float')
    return city_df