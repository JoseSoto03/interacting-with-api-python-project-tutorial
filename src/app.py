import os
import pandas as pd
import seaborn as sns
from dotenv import load_dotenv

# load the .env file variables
load_dotenv()

# Get credential values
client_id = os.environ.get("CLIENT_ID")
client_secret = os.environ.get("CLIENT_SECRET")

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

auth_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
spotify = spotipy.Spotify(auth_manager=auth_manager)

artist_id = "7dGJo4pcD2V6oG8kP0tJRR"

top10_tracks = spotify.artist_top_tracks(artist_id, country="US")

print("Top 10 canciones mas populares")
for idx, track in enumerate(top10_tracks["tracks"][:10]):
    print(f"{idx+1}. {track['name']} - {track['popularity']} de popularidad")
