import requests
import pandas as pd

def fetch_people_data(url):
    names = []
    while url: #tant que l'url est valide et non null on reste dans le while
        response = requests.get(url)
        if response.status_code == 200: #200 équivaut à une requête réussie
            data = response.json()
            names.extend([i['name'] for i in data['results']]) #on ajoute à la liste names chaque valeur qui se situe dans les name(elles même situés dans results)
            url = data['next'] #on affecte l'url qui se situe au endpoint next
        else:
            print(f"Erreur lors de la récupération des données: {response.status_code}")
            break
    return names

def create_names_df(names):
    return pd.DataFrame(names, columns=['Name']) #creation du dataframe


url = 'https://swapi.dev/api/people/'
names = fetch_people_data(url)
names_df = create_names_df(names)
print(names_df)
