#
# This file offers a bunch of functions
# to get specific informations in a dataset
#
# Send global variables from fetch.py as arguments
#
from random import randint


# print error message and return an object {'error': message}
def error(message: str = "internal error"):
    print(f"Error: {message}")
    return {'error': message}


# Gets randomly an album name from the dataset
def getRandomAlbumName(
    artist_albums = None
):
    if artist_albums is None:
        return error("GETRANDOMALBUMNAME - artist_albums is empty")

    index = randint(0, len(artist_albums) - 1)
    return artist_albums[index]['name']


# Returns a set or question/answer about the release year of an album
def getAlbumReleaseYear(
    artist_albums = None,
    name = None
):
    if name is None or artist_albums is None:
        return error("GETALBUMRELEASEYEAR - artist_albums or name is empty")

    release_year = None
    for album in artist_albums:
        if album['name'] == name:
            release_year = album['release_date'][:4]
            break

    if release_year is None:
        return error(f"GETALBUMRELEASEYEAR - coudln't find release year for the album '{name}'")
    return { f"When was the album '{name}' released ?": release_year }

