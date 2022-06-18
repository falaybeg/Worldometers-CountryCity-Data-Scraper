#import pymysql
#from pymongo import MongoClient
#from sqlalchemy import create_engine
import pandas as pd

def mysql_db(country_df, city_df, user, passw, dbName):
    host =  'localhost'
    port = 3306
    user = user #'root'
    passw = passw #'12345'
    dbName = dbName #"LocationData"
    charSet = "utf8mb4"
    cusrorType = pymysql.cursors.DictCursor

    conn = pymysql.connect(host=host, user=user, password=passw, charset=charSet,cursorclass=cusrorType)
    new_db = 'LocationData'
    sql_create_db = "CREATE DATABASE IF NOT EXISTS "+new_db

    cursorObject = conn.cursor() 
    cursorObject.execute(sql_create_db)

    engine = create_engine('mysql+mysqlconnector://'+user+':'+passw+'@'+host+':'+str(port)+'/'+new_db,)
    city_df.to_sql(name='city', con=engine, if_exists = 'replace', index=False)
    country_df.to_sql(name='country', con=engine, if_exists = 'replace', index=False)
    conn.commit()
    print("MySQL - Successfully Saved in Database")
        
def mongodb_save(country_df, city_df, dbName):
    client = MongoClient('mongodb://localhost:27017/')
    db = client[str(dbName)]
    country = db["country"]
    city = db["city"]

    db.country.drop()
    country.insert_many(country_df.to_dict(orient='recors'))
    db.city.drop()
    city.insert_many(city_df.to_dict(orient='recors'))
    print("MongoDB - Successfully Saved in Database")
    
def csv_save(country_df, city_df, country_path, city_path):
    country_df.to_csv(str(country_path), index=False)
    city_df.to_csv(str(city_path), index=False)
    print("CSV - Successfully Saved as CSV File")