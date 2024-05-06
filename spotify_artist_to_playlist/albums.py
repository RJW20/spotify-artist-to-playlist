from collections import namedtuple

import requests


Album = namedtuple('Album', ['id', 'release_date'])

def albums_by_artist(artist_id: str, headers: dict) -> list[Album]:
    """Return a list of all Albums that the Artist with given id has released or featured on."""

    albums = []

    url = f"https://api.spotify.com/v1/artists/{artist_id}/albums?offset=0&limit=50"
    r = requests.get(url, headers=headers)
    data = r.json()
    albums_data = data['items']
    for album in albums_data:
        albums.append(Album(album['id'], album['release_date']))

    # Repeat for any further pages
    while data['next'] is not None:
        url = data['next']
        r = requests.get(url, headers=headers)
        data = r.json()
        albums_data = data['items']
        for album in albums_data:
            albums.append(Album(album['id'], album['release_date']))

    return albums