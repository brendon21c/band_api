from keys import keys
from get_data import *
# import musixmatch.api
#import musixmatch
import requests
import json

#1. you have to get a track id
#2. you send the track id to MM to return lyrics
#3. MM will return the lyrics to the song of the track_id
#Documentation found here: https://developer.musixmatch.com/documentation

def get_track_id(song):

    key = keys['MUSIXMATCH KEY']

    if ' ' in song:

        song  = song.replace(' ', '%20')

    print(song)


    test_search = 'https://api.musixmatch.com/ws/1.1/track.search?callback=callback&q_track={}&quorum_factor=1&apikey={}'.format(song,key)

    #trackName should be a song title
    #this will return a JSON
    request = requests.get(test_search)
    search_json = request.json()

    try:

        trackID = search_json['message']['body']['track_list'][0]['track']['track_id']
        print(trackID)

        return trackID


    except Exception as e:

        return "no id found"


def get_lyrics_for_band(song):

    key = keys['MUSIXMATCH KEY']

    trackID = get_track_id(song)

    test_search = 'https://api.musixmatch.com/ws/1.1/track.lyrics.get?callback=callback&track_id={}&apikey={}'.format(trackID, key)

    #trackName should be a song title
    #this will return a JSON
    request = requests.get(test_search)

    search_json = request.json()


    try:

        lyrics = search_json['message']['body']['lyrics']['lyrics_body']
        print(lyrics)

        return lyrics


    except Exception as e:

        result = "no lyrics found"
