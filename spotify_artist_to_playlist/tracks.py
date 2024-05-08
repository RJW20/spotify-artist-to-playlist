from collections import namedtuple

import requests

from spotify_artist_to_playlist.albums import Album


Track = namedtuple('Track', ['uri', 'name', 'release_date', 'disc_no', 'track_no'])

def tracks_by_album(album: Album, artist_id: str, headers: dict) -> list[Track]:
    """Return a list of all Tracks on the given Album that the Artist with given id has released or featured on."""

    tracks = []

    url = f"https://api.spotify.com/v1/albums/{album.id}/tracks?offset=0&limit=50"
    r = requests.get(url, headers=headers)
    data = r.json()
    tracks_data = data['items']
    for track in tracks_data:

        # Ignore if chosen artist is not attributed
        artist_ids = {artist['id'] for artist in track['artists']}
        if artist_id not in artist_ids:
            continue

        tracks.append(Track(track['uri'], track['name'], album.release_date, track['disc_number'], track['track_number']))

    # Repeat for any further pages
    while data['next'] is not None:
        url = data['next']
        r = requests.get(url, headers=headers)
        data = r.json()
        tracks_data = data['items']
        for track in tracks_data:

            artist_ids = {artist['id'] for artist in track['artists']}
            if id not in artist_ids:
                continue

            tracks.append(Track(track['uri'], track['name'], album.release_date, track['disc_number'], track['track_number']))

    return tracks

def tracks_by_albums(albums: list[Album], artist_id: str, headers: dict) -> list[Track]:
    """Return a list of all Tracks in the given Albums that the Artist with given id has released or featured on."""

    tracks = []
    for album in albums:
        tracks.extend(tracks_by_album(album, artist_id, headers))

    return tracks

def alphabetize(tracks: list[Track]) -> None:
    """Sort the given list of Tracks (in-place) by name (primary) and by release_date (oldest-newest) (secondary)."""

    tracks.sort(key=lambda track: (track.name, track.release_date))
    
def remove_duplicates(tracks: list[Track], version_types: list[str]) -> None:
    """Remove any Tracks with the same names, and attempt to remove any that are of version described in version_types.
    
    When removing duplicates, the Track that appears first in the list is the one that will persist.
    """

    for i in range(len(tracks) - 1):
        
        track = tracks[i]

        # Get a list of all Tracks that start with the same name
        n = len(track.name)
        j = 1
        matches = []
        while i + j < len(tracks) and track.name == tracks[i+j].name[:n]:
            matches.append([j, tracks[i+j]])
            j += 1

        # Remove any direct matches or matches that are of version in version_types
        for j, matching_track in reversed(matches):
            
            # Direct matches
            if len(matching_track.name) == n:
                tracks.pop(i+j)
                continue

            # Versions
            for version_type in version_types:
                if version_type in matching_track.name[n:]:
                    tracks.pop(i+j)
                    break

def chronologize(tracks: list[Track]) -> None:
    """Sort the given list of Tracks (in-place) by release_date (primary), by disc_no (secondary) and by track_no (tertiary)."""

    tracks.sort(key=lambda track: (track.release_date, track.disc_no, track.track_no))