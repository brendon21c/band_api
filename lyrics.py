from keys import keys
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
    musixmatchSEARCH = 'http://api.musixmatch.com/ws/1.1/track.search?q_track={}&format=json'.format(trackName)
    #this will return a JSON
    trackID = 'body.track_list.track.track_id'

    return trackID

def get_lyrics_for_band(band):
    key = keys['MUSIXMATCH KEY']
    musicmatchREQUESTLYRICS =
    'http://api.musixmatch.com/ws/1.1/track.search?q_track={}&format=json'.format(trackName)

  return musicmatchREQUEST



except KeyError:
    pass
