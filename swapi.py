import requests
import pandas as pd
from pandas import json_normalize

# fetch all the starships in the api based on the url in parameters
def get_starships(url):
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

# create a dataframe from a list of starships (names)
def create_starships_df(names):
    return pd.DataFrame(names, columns=['Name'])

# fetch the starship defined with the id in parameters
def get_starship(nombre):
    url = f'https://swapi.dev/api/starships/{nombre}/'
    response = requests.get(url)
    if response.status_code == 200:
        starships = response.json()
        return starships
    else:
        print("Impossible de récupérer les informations car la requête a échoué.")
        return None


#fonction qui récupère tout les noms des personnages de l'API
def get_character(url):
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

#fonction pour créer le dataframe de tout les personnages
def create_names_df(names):
    return pd.DataFrame(names, columns=['Name'])

#fonction qui récupère un personnage suivant l'identifiant qu'on spécifie
def character(nombre):
    url = f'https://swapi.dev/api/people/{nombre}'
    response = requests.get(url)
    if response.status_code == 200: #200 équivaut à une requête réussie
            print(response)
            return response.json()
    else:
            print(f"Erreur lors de la récupération des données: {response.status_code}")

        
