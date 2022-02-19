import pandas as pd
import requests
import datetime

# Get the user_id of the user and the Token from the spotify website
USER_ID = "" # your Spotify username 
TOKEN = "" # your Spotify API token

#Setting up the time so that we can get the last 24 hour's playlist
today = datetime.datetime.now()
yesterday = today - datetime.timedelta(days = 1)
yesterday_unix_time = int(yesterday.timestamp()) * 1000 
GET_URL = 'https://api.spotify.com/v1/me/player/recently-played?after={time}'.format(time=yesterday_unix_time)

headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Authorization": "Bearer {token}".format(token=TOKEN)
    }

def get_playlist(url,headers):

    response = requests.get(url,headers=headers)
    data = response.json()
    
    song_name = []
    artist = []
    album_type = []
    release_date = []
    played_at = []

    for curr_playlist in data["items"]:
            song_name.append(curr_playlist["track"]["name"])
            artist.append(curr_playlist["track"]["artists"][0]["name"])        
            album_type.append(curr_playlist["track"]["album"]["album_type"])
            release_date.append(curr_playlist["track"]["album"]["release_date"])
            played_at.append(curr_playlist["played_at"][0:10])

    

    track_info = {
        "Song" : song_name,
        "Artists" : artist,
        "album_type":album_type,
        "release_date":release_date,
        "Played_at":played_at

     }

    return track_info

def main():
    track_info_dict = get_playlist(GET_URL,headers)
    track_info_df = pd.DataFrame (track_info_dict, columns = ['Song','Artists','album_type','release_date','Played_at'])
    print(track_info_df)
    return track_info_df
