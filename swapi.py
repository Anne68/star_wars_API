import requests
import pandas as pd
from pandas import json_normalize

def request_test(url):
    names = []
    while url:
        response = requests.get(url)
        if response.status_code == 200:
            starships = response.json()
            names.extend([i['name'] for i in starships['results']])
            url = starships['next']
        else:
            print(f"La requête a échoué avec le code d'état {response.status_code}")
            break
    return names

def create_names_df(names):
    return pd.DataFrame(names, columns=['Name'])

def request_info(nombre):
    url = f'https://swapi.dev/api/starships/{nombre}/'
    response = requests.get(url)
    if response.status_code == 200:
        starships = response.json()
        return starships
    else:
        print("Impossible de récupérer les informations car la requête a échoué.")
        return None

url = 'https://swapi.dev/api/starships/'
names = request_test(url)
names_df = create_names_df(names)
print(names_df)

response_info = request_info('15')
if response_info:
    df_character = json_normalize(response_info)
    print("Vaisseau de Star Wars :")
    print(df_character)
else:
    print("Erreur lors de la récupération des informations.")
