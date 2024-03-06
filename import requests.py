import requests
import pandas as pd

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

# Appeler la fonction en lui passant l'URL de l'API
url = "https://swapi.dev/api/vehicles/"
response_data = interroger_api(url)

if response_data is not None:
    # Créer un DataFrame à partir des données
    df_vehicles = pd.DataFrame(response_data)
    print(df_vehicles)
else:
    print("Pas de données à afficher.")
