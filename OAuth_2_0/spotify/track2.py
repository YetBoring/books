#!/usr/bin/env python3

import os
import requests
import base64
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Spotify API credentials
client_id = os.getenv('CLIENT_ID')
client_secret = os.getenv('CLIENT_SECRET')

# Encode the client ID and client secret
auth_str = f"{client_id}:{client_secret}"
b64_auth_str = base64.b64encode(auth_str.encode()).decode()

# Token URL
url = 'https://accounts.spotify.com/api/token'

# Make a POST request to get the access token
response = requests.post(url, headers={
    "Authorization": f"Basic {b64_auth_str}"
}, data={
    "grant_type": "client_credentials"
})

# Parse the JSON response
token = response.json().get('access_token')
print(f"Access Token: {token}")

# Track ID
track_id = '3n3Ppam7vgaVa1iaRUc9Lp'  # Example track ID

# Spotify endpoint for track details
url = f'https://api.spotify.com/v1/tracks/{track_id}'

# Make the GET request with the access token
response = requests.get(url, headers={
    "Authorization": f"Bearer {token}"
})

# Parse and print the response
track = response.json()

print(f"Track Name: {track['name']}")
print(f"Artist: {track['artists'][0]['name']}")
print(f"Album: {track['album']['name']}")
print(f"Popularity: {track['popularity']}")


