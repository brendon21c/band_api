from keys import keys
from data_processing import *
import requests
from logging import log

base_url = 'https://app.ticketmaster.com/discovery/v2/events.json?apikey={}&keyword={}&stateCode=MN'


def get_dates_for_artist(artist):

    key = keys['TM_KEY']

    url = base_url.format(key, artist)

    response = requests.get(url)

    TM_process(response)

    # tm_json = response.json()
    #
    # # process this somehow
    #
    # data = TM_process(tm_json)




def TM_process(url):

    tm_json = url.json()

    info_list = []

    try:

        artist = tm_json["_embedded"]['events'][0]
        print(artist['url']) # ticket infor url
        venue = artist["_embedded"]['venues'][0] # Gets venue
        print(venue['name'])
        info_list.append(artist['url'])
        info_list.append(venue['name'])

        return info_list


    except Exception as e:

        #log.error("problem", e) # throwing an error

        # no_artist_found = "Sorry, that artist is not playing Minnesoata at this time."

        ## return an empty list if no results found

        #info_list.append(no_artist_found)

        return info_list
