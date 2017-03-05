from keys import keys
from get_data import *
import musixmatch.api
import musixmatch
import urllib.request
import requests
import json

#1. you have to get a track id
#2. you send the track id to MM to return lyrics
#3. MM will return the lyrics to the song of the track_id
#Documentation found here: https://developer.musixmatch.com/documentation
def get_track_id(trackID):
    key = keys['MUSIXMATCH KEY']
    trackName =
    musixmatchSEARCH = 'http://api.musixmatch.com/ws/1.1/track.search?q_track={}&format=json'.format(trackName)
    #trackName should be a song title
    #this will return a JSON

    trackID = musixmatchSEARCH.'body.track_list.track.track_id'
    #need the trackID to send to musixmatch in order to get lyrics

    return trackID

def get_lyrics_for_band(band):
    key = keys['MUSIXMATCH KEY']
    trackID = get_track_id()

    musicmatchREQUESTLYRICS =
    'http://api.musixmatch.com/ws/1.1/track.lyrics.get?track_id={}&format=json'.format(trackID)

    lyrics = musicmatchREQUESTLYRICS.'body.lyrics.lyrics_body'

  return lyrics
