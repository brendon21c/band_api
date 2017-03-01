from keys import keys
import requests

base_url = 'https://app.ticketmaster.com/discovery/v2/events.json?apikey={}&keyword={}&stateCode=MN'


def get_dates_for_artist(artist):

    key = keys['TM_KEY']

    url = base_url.format(key, artist)

    response = requests.get(url)

    tm_json = response.json()

    # process this somehow

    data = process(tm_json)

    return data


def process(tm_json):
    pass  # todo 
