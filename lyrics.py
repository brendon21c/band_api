from keys import keys
from get_data import *
# import musixmatch.api
# import musixmatch
import urllib.request
import requests
import json

#1. you have to get a track id
#2. you send the track id to MM to return lyrics
#3. MM will return the lyrics to the song of the track_id
#Documentation found here: https://developer.musixmatch.com/documentation
def get_track_id(song):
    key = keys['MUSIXMATCH KEY']

    #trackName = get_data_for_band(song)
    musixmatchSEARCH = 'http://api.musixmatch.com/ws/1.1/track.search?q_track={}'.format(song)
    print(musixmatchSEARCH)
    #trackName should be a song title
    #this will return a JSON
    request = requests.get(musixmatchSEARCH)
    search_json = request.json()
    print(search_json)

    #trackID = musixmatchSEARCH.'body.track_list.track.track_id'
    trackID = search_json['body']['track_list'][0]
    print(trackID)

    #need the trackID to send to musixmatch in order to get lyrics

return trackID

def get_lyrics_for_band(song):

    key = keys['MUSIXMATCH KEY']

    trackID = get_track_id(song)

    musicmatchREQUESTLYRICS = 'http://api.musixmatch.com/ws/1.1/track.lyrics.get?track_id={}&format=json'.format(trackID)

    #lyrics = musicmatchREQUESTLYRICS.'body.lyrics.lyrics_body'

    return lyrics
