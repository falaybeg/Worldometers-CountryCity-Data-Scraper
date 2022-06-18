import pandas as pd
import requests
from bs4 import BeautifulSoup
from country_data import *
from city_data import *
from database_config import *

# Scrappign County and City Data
country_df = get_country_data()
city_df = get_city_data(country_df)

# You can print scraped data as dataframe
#print(country_df.head())
#print(city_df.head())

print("***Export Data***\n1. MySQL Database\n2.MongoDB\n3.CSV File")
choice = int(input("Choice: "))

if(choice == 1):
    user ='root'
    passw = '12345'
    dbName = 'LocationData'
    mysql_db(country_df, city_df, user, passw, dbName)
elif(choice == 2):
    dbName = 'LocationDatabase'
    mongodb_save(country_df, city_df,dbName)
elif(choice == 3):
    country_path = "Worldometers-CountryCity-Data-Scraper/data/country_data.csv"
    city_path = "Worldometers-CountryCity-Data-Scraper/data/city_data.csv"
    csv_save(country_df, city_df, country_path, city_path)
else: 
    print("\nWrong Choice!\nPlease try again!")    
  
