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
from spotipy.oauth2 import SpotifyOAuth

bl = "***----------------------------------------------------------***"

### Spotipy Setup ###
client_secret_key = os.environ['SPOTIPY_SECRET_KEY']

scope = "user-top-read"
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id="eb51bb11a7be4beaa72fe42192bd38cf",
                                            client_secret=client_secret_key,
                                            redirect_uri="http://localhost:8888/callback",
                                            scope=scope))


'''playlists = sp.current_user_playlists(limit=3)
print(playlists)

for playlist in playlists['items']:
    print(playlist['name'])'''
###

def get_spotify_artists(ofst):
    top_art = sp.current_user_top_artists(limit=10, offset=ofst, time_range='long_term')

    get_top_ten(ofst, top_art)

    inp = input('Hit enter to see next ten! (Up to 200...)\n')
    if inp != "":
        ofst = 0
        spotidata_interface()
    else:
        get_spotify_artists(ofst=(ofst + 10))



def get_spotify_tracks(ofst):
    top_tr = sp.current_user_top_tracks(limit=10, offset=ofst, time_range='long_term')

    get_top_ten(ofst, top_tr)

    inp = input('Hit enter to see next ten! (Up to 200...)\n')
    if inp != "":
        ofst = 0
        spotidata_interface()
    else:
        get_spotify_tracks(ofst=(ofst + 10))


def get_top_ten(ofst, top):
    print("\nHere they are!\n")
    for i, artist in enumerate(top['items']): 
        print("  ", f"{i + 1 + ofst}.", artist['name'])
    print("\n", bl)  


def spotidata_interface():
    print("\n", bl,
          "\nPlease Select from the options below!\n\n",
          "1. See Top 10 Artists\n",
          "2. See Top 10 Tracks\n",
          "3. See Track Info\n")
    inp = input("")
    
    if inp == "1":
        get_spotify_artists(ofst=0)
    elif inp == "2":
        get_spotify_tracks(ofst=0)
    else:
        print("Sorry! This option is not available yet. :(")
        spotidata_interface()
    


def main():
    print("\n", bl)
    print("Hello, welcome to spotidata!\n")
    spotidata_interface()
    #get_spotify_artists(ofst=0)

if __name__=="__main__":
    main()



