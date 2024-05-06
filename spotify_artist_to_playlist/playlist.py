import json

import requests


def create_playlist(user_id: int, name: str, artist_name: str, headers: dict) -> str:
    """Create a Playlist with the given name on the Spotify account with the given user_id and 
    then return the id of the Playlist."""

    payload = {
        'name': name,
        'description': f'A playlist containing all non-duplicate songs released by {artist_name}, ' + \
            'created using https://github.com/RJW20/spotify-artist-to-playlist.',
    }
    
    url = f'https://api.spotify.com/v1/users/{user_id}/playlists'
    r = requests.post(url, headers=headers, data=json.dumps(payload))
    data = r.json()

    return data['id']