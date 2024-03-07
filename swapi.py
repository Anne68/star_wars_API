import requests
import pandas as pd
from pandas import json_normalize

#récupère une planète
def fetch_planet(nmb):
    api_url = f"https://swapi.tech/api/planets/{nmb}"
    response = requests.get(api_url)
    if response.status_code == 200:
        planet = response.json()
        return planet
    else:
        print("Impossible de récupérer les informations car la requête a échoué.")
        return None

#recupère toutes les planètes
def fetch_all_planets(api_url="https://swapi.tech/api/planets/", planets=None):
    if planets is None:
        planets = []
    response = requests.get(api_url)
    if response.status_code == 200:
        data = response.json()
        planets.extend(data['results'])
        if data['next']:
            return fetch_all_planets(data['next'], planets)
        else:
            return planets
    else:
        print("Impossible de récupérer les informations car la requête a échoué.")
        return planets

#créer le dataframe pour afficher les planètes en fonction de leur diamètre
def display_planet_dataframe():
    planets = fetch_all_planets()
    planet_df = pd.DataFrame(planets)
    planet_df['diameter'] = pd.to_numeric(planet_df['diameter'], errors='coerce').fillna(-1)
    sorted_planet_df = planet_df.sort_values(by='diameter', ascending=False)
    print(sorted_planet_df[['name', 'diameter']])

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
    url = f'https://swapi.tech/api/starships/{nombre}/'
    response = requests.get(url)
    if response.status_code == 200:
        starships = response.json()
        return starships
    else:
        print("Impossible de récupérer les informations car la requête a échoué.")
        return None


#fonction qui récupère tout les noms des personnages de l'API
def get_characters(url):
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
def get_character(nombre):
    url = f'https://swapi.tech/api/people/{nombre}'
    response = requests.get(url)
    if response.status_code == 200: #200 équivaut à une requête réussie
            print(response)
            return response.json()
    else:
            print(f"Erreur lors de la récupération des données: {response.status_code}")


def interroger_api(url):
    response = requests.get(url)

    if response.status_code == 200:
        # Convertir la réponse JSON en un dictionnaire Python
        data = response.json()
        # Renvoyer les données
        return data
    else:
        # Afficher un message d'erreur si la requête a échoué
        print("La requête a échoué avec le code d'état :", response.status_code)
        # Renvoyer None pour indiquer une absence de données en cas d'erreur
        return None
