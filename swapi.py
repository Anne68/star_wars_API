import requests
import pandas as pd

def fetch_data(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

def get_perso(url, perso_liste):
    data = fetch_data(url)
    if data:
        perso_liste.extend(data['results'])
        next_page = data['next']
        if next_page:
            get_perso(next_page, perso_liste)

base_url = 'https://swapi.dev/api/people/'
perso = []
get_perso(base_url, perso)

perso_df = pd.DataFrame(perso)
print(perso_df)
