''' Code for later...

from openai import OpenAI
client = OpenAI()

def find_dupes():

def create_playlist():

def ai_song_request():

Spotipy documentation: https://spotipy.readthedocs.io/en/2.24.0/ 
Spotify Web API: https://developer.spotify.com/documentation/web-api/reference/get-playlist 
Open AI API: https://platform.openai.com/docs/guides/chat-completions 


venv activate path: .\.venv\Scripts\activate

setx SPOTIPY_SECRET_KEY your_client_secret_here
'''
from openai import OpenAI
import spotipy
# import openai
import os
from spotipy.oauth2 import SpotifyOAuth
import pandas as pd

bl = "***----------------------------------------------------------***"

### Spotipy Setup ###

# print(os.environ.get('SPOTIPY_SECRET_KEY'))
client_secret_key = os.environ['SPOTIPY_SECRET_KEY']

scope = "user-top-read user-library-read playlist-read-private"
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id="eb51bb11a7be4beaa72fe42192bd38cf",
                                            client_secret=client_secret_key,
                                            redirect_uri="http://localhost:8888/callback",
                                            scope=scope))

username = sp.current_user()

'''playlists = sp.current_user_playlists(limit=3)
print(playlists)

for playlist in playlists['items']:
    print(playlist['name'])'''
###


### Openai Setup ###
client = OpenAI()
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


def get_playlist():
    spotdict = {}
    spotlistnames = []
    spotlist = [['Track', 'Album', 'Artist', 'Genres', 'Popularity']]
    list_name = "No Skips" # input("\nPlease enter a playlist name: ")
    playlists = sp.current_user_playlists()
    

    for playlist in playlists['items']:
        if playlist['name'] == list_name:
            list_name_id = playlist['id']
            name_found = True

    if name_found == False:
        print("Oops, that name is not found.")
        #spotidata_interface()
        get_playlist()

    spotlistfull = sp.user_playlist_tracks(username, playlist_id=list_name_id, )
    print(len(spotlistfull['items']))
    while len(spotlistfull['items']) > 0:
        print(len(spotlistfull['items']))
        for song in (spotlistfull['items']): 
            spotlistnames.append(song['track']['name'])
            print(song['track']['name'], song['track']['is_local'])
            if song['track']['is_local'] == False:
                genres = get_track_genre(song['track']['artists'][0]['id'])
            spotdict[song['track']['name']] = {"name": {"name": song['track']['name'], "id": song['track']['id']},
                                            "album": {"name": song['track']['album']['name'], "id": song['track']['album']['id']},
                                            "artists": {"name": song['track']['artists'][0]['name'], "id": song['track']['artists'][0]['id']},
                                            "genres": genres,
                                            "popularity": song['track']['popularity']}
            spotlist.append([song['track']['name'],
                            song['track']['album']['name'],
                            song['track']['artists'][0]['name'],
                            genres,
                            song['track']['popularity']])
            
        spotlistfull = sp.next(spotlistfull)
    
    for songname in spotlistnames:
        print(f"{', '.join((spotdict[songname]['name']['name'], spotdict[songname]['artists']['name']))};  Genres: {', '.join(spotdict[songname]['genres'])}")

    print("\n", bl)

    spottable = pd.DataFrame(spotlist[1:], columns=spotlist[0])

    print(spottable.to_string())


def get_track_genre(artistid):
    print("YEs")
    artist = sp.artist(artist_id=artistid)
    
    return artist['genres']

def ai_integration():
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair."},
            {"role": "user", "content": "Compose a poem that explains the concept of recursion in programming."}
        ]
    )

    print(completion.choices[0].message)

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
          "3. See Playlist\n")
    inp = input("")
    
    if inp == "1":
        get_spotify_artists(ofst=0)
    elif inp == "2":
        get_spotify_tracks(ofst=0)
    elif inp == "3":
        get_playlist()
    else:
        print("Sorry! This option is not available yet. :(")
        spotidata_interface()
    


def main():
    print("\n", bl)
    print("Hello, welcome to spotidata!\n")
    #spotidata_interface()
    #get_spotify_artists(ofst=0)
    #get_playlist()
    get_track_genre(artistid="2YZyLoL8N0Wb9xBt1NhZWg")

if __name__=="__main__":
    main()



