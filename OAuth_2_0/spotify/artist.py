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

artist_name = 'Adele'
results = sp.search(q=f'artist:{artist_name}', type='artist')
artist = results['artists']['items'][0]
print(artist)
print(f"Artist Name: {artist['name']}")
print(f"Followers: {artist['followers']['total']}")
print(f"Genres: {', '.join(artist['genres'])}")

artist_id = artist['id']
top_tracks = sp.artist_top_tracks(artist_id)

print(f"Top tracks of {artist_name}")
for track in top_tracks['tracks']:
    print(f"Track Name: {track['name']}, Popularity: {track['popularity']}")
