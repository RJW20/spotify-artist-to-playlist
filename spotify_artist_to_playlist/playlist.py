import json
from itertools import batched

import requests

from spotify_artist_to_playlist.tracks import Track


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


def add_tracks(playlist_id: str, tracks: list[Track], headers: dict) -> None:
    """Post all the given Tracks to the Playlist with given playlist_id."""

    url = f'https://api.spotify.com/v1/playlists/{playlist_id}/tracks'
    track_uris = [track.uri for track in tracks]
    for batch in batched(track_uris, 100):
        requests.post(url, headers=headers, data=json.dumps(batch))
                                  
    return
