from collections import namedtuple

import requests


Artist = namedtuple('Artist', ['id', 'name'])

def get_artist(artist_id: str, headers: dict) -> Artist:
    """Return the full Artist object for the Artist with given id."""

    url = f"https://api.spotify.com/v1/artists/{artist_id}"
    r = requests.get(url, headers=headers)
    data = r.json()

    return Artist(artist_id, data['name'])