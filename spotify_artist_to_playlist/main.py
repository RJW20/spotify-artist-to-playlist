from spotify_artist_to_playlist.settings import settings
from spotify_artist_to_playlist.authentication import get_token, get_user_id
from spotify_artist_to_playlist.artist import get_artist
from spotify_artist_to_playlist.albums import albums_by_artist
from spotify_artist_to_playlist.tracks import tracks_by_albums, alphabetize, remove_duplicates, chronologize
from spotify_artist_to_playlist.playlist import create_playlist, add_tracks


def main() -> None:

    headers = {'accept': "application/json"}
    auth_token_header = get_token(settings['sp_dc_cookie'])
    headers.update(auth_token_header)

    user_id = get_user_id(headers)

    artist = get_artist(settings['artist_id'], headers)

    version_types = settings['unwanted_versions']
    
    albums = albums_by_artist(artist.id, headers)
    tracks = tracks_by_albums(albums, artist.id, headers)
    alphabetize(tracks)
    remove_duplicates(tracks, version_types)
    chronologize(tracks)

    headers = {'Content-Type': 'application/json'}
    headers.update(auth_token_header)

    playlist_id = create_playlist(user_id, artist.name, artist.name, headers)
    add_tracks(playlist_id, tracks, headers)


if __name__ == '__main__':
    main()