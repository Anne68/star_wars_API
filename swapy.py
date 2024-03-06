import requests
import pandas as pd
from pandas import json_normalize

def fetch_star_wars_data(nmb):
    api_url = f"https://swapi.dev/api/planets/{nmb}"
    response = requests.get(api_url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        print(response)
        # Check if 'results' key exists in the data
        return response.json()
    else:
        print(f"Error: Failed to fetch data. Status Code: {response.status_code}")
        return None

if __name__ == "__main__":
    star_wars_data = fetch_star_wars_data("2")

    # Check if star_wars_data is not None before proceeding
    if star_wars_data:
        star_wars_df = json_normalize(star_wars_data)

        print(star_wars_df)

import requests
import pandas as pd

def fetch_planet_data():
    api_url = "https://swapi.dev/api/planets/"
    response = requests.get(api_url)

    if response.status_code == 200:
        data = response.json()
        # Extracting relevant information (planet name and size) from the API response
        planet_data = [{'Name': planet['name'], 'Size': int(planet['diameter'])} for planet in data['results']]
        return planet_data
    else:
        print(f"Error: Failed to fetch data. Status Code: {response.status_code}")
        return None

def display_planet_dataframe():
    planet_data = fetch_planet_data()

    if planet_data:
        # Creating a DataFrame from the extracted planet data
        planet_df = pd.DataFrame(planet_data)
        # Sorting the DataFrame by planet size in descending order
        sorted_planet_df = planet_df.sort_values(by='Size', ascending=False)

        # Displaying the sorted DataFrame
        print(sorted_planet_df)

if __name__ == "__main__":
    display_planet_dataframe()
