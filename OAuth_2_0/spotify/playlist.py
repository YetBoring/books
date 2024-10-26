#!/usr/bin/env python3

import click
import os
import spotipy
from dotenv import load_dotenv
from spotipy.oauth2 import SpotifyOAuth


# Load environment variables from .env file
load_dotenv()

@click.command()
def get_playlists():
    # Spotify API credentials
    client_id = os.getenv('CLIENT_ID')
    client_secret = os.getenv('CLIENT_SECRET')
    redirect_uri = 'http://localhost:8888/callback'

    # Authentication
    sp_oauth = SpotifyOAuth(
        client_id=client_id,
        client_secret=client_secret,
        redirect_uri=redirect_uri,
        scope="playlist-read-private"
    )

    # URL for user authentication
    auth_url = sp_oauth.get_authorize_url()
    print(f"Please navigate to the following URL to authenticate:\n{auth_url}")

    # Get the token after authentication
    response_url = input("Paste the URL you were redirected to here: ")
    code = sp_oauth.parse_response_code(response_url)
    token_info = sp_oauth.get_access_token(code)

    if token_info:
        sp = spotipy.Spotify(auth=token_info['access_token'])
        playlists = sp.current_user_playlists()
        print(f"Total number of playlist: {len(playlists['items'])}")
        for playlist in playlists['items']:
            print(f"Playlist: {playlist['name']} - Total Tracks: {playlist['tracks']['total']}")

if __name__ == '__main__':
    get_playlists()



