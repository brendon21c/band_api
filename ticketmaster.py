from keys import keys
from data_processing import *
import requests
from logging import log

base_url = 'https://app.ticketmaster.com/discovery/v2/events.json?apikey={}&keyword={}&stateCode=MN'


def get_dates_for_artist(artist):

    key = keys['TM_KEY']

    url = base_url.format(key, artist)

    response = requests.get(url)

    tm_json = response.json()

    info_list = []

    try:

        artist = tm_json["_embedded"]['events'][0]
        print(artist['url']) # ticket infor url
        venue = artist["_embedded"]['venues'][0] # Gets venue
        print(venue['name'])
        info_list.append(artist['url'])
        info_list.append(venue['name'])

        print(info_list)

        return info_list


    except Exception as e:

        
        return info_list
