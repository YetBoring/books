#!/usr/bin/env python3

import click
import os
import spotipy
from dotenv import load_dotenv
from http.server import BaseHTTPRequestHandler, HTTPServer
from spotipy.oauth2 import SpotifyOAuth


# Load environment variables from .env file
load_dotenv()

# Spotify API credentials
client_id = os.getenv('CLIENT_ID')
client_secret = os.getenv('CLIENT_SECRET')
redirect_uri = 'http://localhost:8888/callback'

class AuthHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        global code
        query = self.path.split('?', 1)[-1]
        params = dict(p.split('=') for p in query.split('&'))

        if 'code' in params:
            code = params['code']
        # Redirect user's browser to Spotify home page
        # self.send_response(303)
        # self.send_header('Location', 'https://www.spotify.com/')
        # self.end_headers()

@click.command()
def get_playlists():
    # Authentication
    sp_oauth = SpotifyOAuth(
        client_id=client_id,
        client_secret=client_secret,
        redirect_uri=redirect_uri,
        scope="playlist-read-private",
        open_browser=True
    )

    server = HTTPServer(("localhost", 4321), AuthHandler)
    server.timeout = None


    # URL for user authentication
    auth_url = sp_oauth.get_authorize_url()
    print(f"Please navigate to the following URL to authenticate:\n{auth_url}")

    # server.handle_request()

    # Get the token after authentication
    response_url = input("Paste the URL you were redirected to here: ")
    code = sp_oauth.parse_response_code(response_url)
    token_info = sp_oauth.get_access_token(code)

    if token_info:
        print(token_info)
        sp = spotipy.Spotify(auth=token_info['access_token'])
        # sp = spotipy.Spotify(auth=token_info)
        playlists = sp.current_user_playlists()
        print(f"Total number of playlist: {len(playlists)")
        for playlist in playlists['items']:
            print(f"Playlist: {playlist['name']} - Total Tracks: {playlist['tracks']['total']}")

if __name__ == '__main__':
    get_playlists()



