# Spotify Artist to Playlist
A python script that takes an artist on Spotify and creates a playlist on your Spotify account containing all of their non-duplicate songs, sorted by album. Also allows 
you to choose to not include certain versions (e.g. acoustic, live) or remixes.

## Requirements
1. [Python](https://www.python.org/downloads/).
2. [Poetry](https://python-poetry.org/docs/) for ease of installing the dependencies.
3. The id of the artist you wish to create the playlist for - if you find them on spotify then the url will be of the form https://open.spotify.com/artist/*artist_id*.
4. Your sp_dc Spotify cookie - can be found by logging in to spotify on Chrome then going to  `More tools/Developer tools` -> `Application/Storage/Cookies/https://open.spotify.com`.

## Running the Script
1. Clone or download the repo `git clone https://github.com/RJW20/spotify-artist-to-playlist.git`.
2. Set up the virtual environment `poetry install`.
3. Enter the virtual environment `poetry shell`.
4. Enter your settings in `settings.py` - unwanted versions should have a leading capital letter.
5. Run the script `poetry run main`.