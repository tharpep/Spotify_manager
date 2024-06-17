''' Code for later...

from openai import OpenAI
client = OpenAI()

completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair."},
    {"role": "user", "content": "Compose a poem that explains the concept of recursion in programming."}
  ]
)

print(completion.choices[0].message)

def find_dupes():

def create_playlist():

def ai_song_request():




'''

import spotipy
import openai
import os
from spotipy.oauth2 import spotifyOAuth

client_secret_key = os.environ['SPOTIPY_SECRET_KEY']
print(client_secret_key)

def main():
    spotipy_setup()

if __name__=="__main__":
    main()



def spotipy_setup():
    scope = "playlist-modify-prive playlist-read-private"
    sp = spotipy.Spotify(auth_manager=spotifyOAuth(client_id="eb51bb11a7be4beaa72fe42192bd38cf",
                                                client_secret=client_secret_key,
                                                redirect_uri="http://localhost:8888/callback",
                                                scope=scope))


    playlists = sp.current_user_playlists()