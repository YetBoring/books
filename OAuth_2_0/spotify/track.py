#!/usr/bin/env python3

import os
import spotipy
from dotenv import load_dotenv
from spotipy.oauth2 import SpotifyClientCredentials

# Load environment variables from .env file
load_dotenv()

# Spotify API credentials
client_id = os.getenv('CLIENT_ID')
client_secret = os.getenv('CLIENT_SECRET')

# Set up client credentials manager
auth_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(auth_manager=auth_manager)

track_id = '3n3Ppam7vgaVa1iaRUc9Lp'  # Example track ID
track = sp.track(track_id)
print(f"Track Name: {track['name']}")
print(f"Artist: {track['artists'][0]['name']}")
print(f"Album: {track['album']['name']}")
print(f"Popularity: {track['popularity']}")


