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
