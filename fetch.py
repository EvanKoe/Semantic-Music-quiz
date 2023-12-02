import requests
import json
from random import randint
import os
from dotenv import load_dotenv

# load .env values
load_dotenv()

import spotipy
from spotipy.oauth2 import SpotifyOAuth

scope = "user-top-read"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

band_objects = []
selected_artist = None


# Gets twenty bands from your spotify profile
def getTwentyRandomArtists():
    global band_objects
    band_list = []
    band_objects = sp.current_user_top_artists(limit=20, offset=randint(0, 32))

    # If getting an artist fails
    if band_objects is None or band_objects  == []:
        print("Error getting artists")
        return None

    # Getting a list with only names
    for artist in band_objects['items']:
        band_list.append(artist["name"])

    band_objects = band_objects['items']
    return band_list


# Fetch information from band
def fetchInfoFromBand(name: str = ""):
    global band_objects, selected_artist
    if name == "":
        return {"error": "Empty band name"}

    if band_objects is None or band_objects == []:
        print(f"Error: the band '{name}' was not in the list.")
        return {'error': f"the band {name} was not in the list"}

    band_item = None
    for band in band_objects:
        if band['name'] == name:
            band_item = band
            break

    if band_item is None:
        print(f"Error: The band '{name}' was not in the list.")
        return {'error': f"the band {name} was not in the list"}

    selected_artist = sp.artist(band_item['id'])
    return selected_artist


# Generates a set of questions about the selected_artist
def generateQuestions(name: str = ""):
    global selected_artist

    if name == "":
        print("Error: empty band")
        return {'error': 'Empty band'}

    fetchInfoFromBand(name)
    return None


artists = getTwentyRandomArtists()
if artists is None:
    print("Error: Artists is None")
    exit(84)
fetchInfoFromBand(artists[0])

