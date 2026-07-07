"""This script handles interaction with the omdb api to fetch movie data
before passing it on to the Flask routes."""

import os
import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv('API_KEY')
REQUEST_URL = "https://www.omdbapi.com/"

def get_movie_from_omdb(title, year=None):
    """ Fetches movie data from OMDB API. If a year argument is provided,
    it is added to the api request."""
    try:
        params = {
            "apikey": API_KEY,
            "t": title
        }

        if year:
            params["y"] = year

        response = requests.get(REQUEST_URL,
                                params=params,
                                timeout=5)

        response.raise_for_status()

        data = response.json()

        if data.get("Response") == "False":
            return None

        return {
            "name": data["Title"],
            "director": data["Director"],
            "year": int(data["Year"]) if data["Year"].isdigit() else None,
            "imdb_id": data["imdbID"],
            "poster_url": None if data["Poster"] == "N/A" else data["Poster"],
        }

    except requests.exceptions.RequestException:
        return None
