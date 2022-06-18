import pandas as pd
import requests
from bs4 import BeautifulSoup


def scrapping_country_data():
    url = "https://www.worldometers.info/world-population/population-by-country/"
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")


    population_data = []
    population_header = ['country_id','country_name', 'population', 'yearly_change_percent', 'Net_Change',
                        'Density_(P/Km2)','Land_Area_(Km2)', 'Migrants_net', 'Fert_Rate',  'Med_Age',
                        'Urban_Pop_percent', 'World_Share']

    for row in soup.select('tbody tr'):
        row_text = [x.text for x in row.find_all('td')]
        population_data.append(row_text)        
    
    country_df = pd.DataFrame(population_data, columns=population_header)
    return country_df


def get_country_data():
    country_df = scrapping_country_data()
    country_df["population"] = country_df['population'].replace(',','', regex=True)
    country_df["yearly_change_percent"] = country_df['yearly_change_percent'].replace('%','', regex=True)
    country_df["Net_Change"] = country_df['Net_Change'].replace(',','', regex=True)
    country_df["Density_(P/Km2)"] = country_df['Density_(P/Km2)'].replace(',','', regex=True)
    country_df["Land_Area_(Km2)"] = country_df['Land_Area_(Km2)'].replace(',','', regex=True)
    country_df["Migrants_net"] = country_df['Migrants_net'].replace(',','', regex=True)
    country_df["Migrants_net"] = country_df['Migrants_net'].replace(' ',None, regex=True)
    country_df["World_Share"] = country_df['World_Share'].replace('%','', regex=True)
    country_df["Fert_Rate"] = country_df['Fert_Rate'].replace('N.A.',None, regex=True)
    country_df["Med_Age"] = country_df['Med_Age'].replace('N.A.',None, regex=True)
    country_df["Urban_Pop_percent"] = country_df['Urban_Pop_percent'].replace('N.A.',None, regex=True)
    country_df["Urban_Pop_percent"] = country_df['Urban_Pop_percent'].replace('%','', regex=True)
    country_df['country_id'] = country_df['country_id'].astype('int')
    country_df['population'] = country_df['population'].astype('float')
    country_df['Net_Change'] = country_df['Net_Change'].astype('float')
    country_df['yearly_change_percent'] = country_df['yearly_change_percent'].astype('float')
    country_df['Density_(P/Km2)'] = country_df['Density_(P/Km2)'].astype('int')
    country_df['Fert_Rate'] = country_df['Fert_Rate'].astype('float')
    country_df["Med_Age"] = country_df["Med_Age"].fillna(value='0')
    country_df['Med_Age'] = country_df['Med_Age'].astype('int')
    country_df['Land_Area_(Km2)'] = country_df['Land_Area_(Km2)'].astype('int')
    country_df["Migrants_net"] = country_df['Migrants_net'].astype('float')
    country_df['Urban_Pop_percent'] = country_df['Urban_Pop_percent'].astype('float')
    country_df['World_Share'] = country_df['World_Share'].astype('float')
    return country_df