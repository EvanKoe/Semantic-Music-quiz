from random import randint
from dotenv import load_dotenv

from lib import getAlbumReleaseYear, getRandomAlbumName

# load .env values
load_dotenv()

import spotipy
from spotipy.oauth2 import SpotifyOAuth


# Spotipy object
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope="user-top-read"))


# Global variables
band_objects = []
selected_artist = None
selected_artist_albums = []


# Gets twenty bands from your spotify profile
def getTwentyRandomArtists():
    global band_objects
    band_list = []
    band_objects = sp.current_user_top_artists(limit=20, offset=randint(0, 32))

    if band_objects is None or band_objects  == []:
        print("Error getting artists")
        return None

    for artist in band_objects['items']:
        band_list.append(artist["name"])

    band_objects = band_objects['items']
    return band_list


# Get full artist object from name
def getArtistItemByName(name: str = ""):
    global band_objects

    if name == "":
        print("Error: empty band name")
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

    return band_item


# Fetch information from band
def fetchInfoFromBand(name: str = ""):
    global band_objects, selected_artist, selected_artist_albums
    if name == "":
        print("Error: empty band name")
        return {"error": "Empty band name"}

    band_item = getArtistItemByName(name)
    selected_artist = sp.artist(band_item['id'])
    result = sp.artist_albums(band_item['id'], album_type='album')

    if result is None:
        print("Warning: couldn't get albums")
        return None

    selected_artist_albums = result['items']
    return {'message': 'success'}


# Generates a set of questions about the selected_artist
def generateQuestions(name: str = ""):
    global selected_artist, artist_albums
    questions = []

    if name == "":
        print("Error: empty band")
        return {'error': 'Empty band'}

    fetchInfoFromBand(name)
    questions.append(getAlbumReleaseYear(
        selected_artist_albums,
        getRandomAlbumName(selected_artist_albums)
    ))
    return questions
