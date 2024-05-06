from collections import namedtuple

import requests


Artist = namedtuple('Artist', ['id', 'name'])

def albums_by_artist(artist_id: str, headers: dict) -> Artist:
    """Return the full Artist object for the Artist with given id."""

    url = f"https://api.spotify.com/v1/artists/{artist_id}"
    r = requests.get(url, headers=headers)
    data = r.json()
    return Artist(id, data['name'])