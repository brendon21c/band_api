from keys import keys
from ticketmaster import *
from band_images import *
from lyrics import *


def get_data_for_band(band):

    # At the moment, make three requests, one after the other
    # Future: make all three request concurrently
    # Future: check cache for info before making requests

    # todo get data from ticketmaster. Return data in suitable format for template
    ticketmaster_data = get_dates_for_artist(band)
    print(ticketmaster_data)

    # todo get data from image source Return data in suitable format for template
    photos = get_photos_for_band(band)

    return ticketmaster_data, photos

def get_lyrics_for_song(song):

    lyrics = get_lyrics_for_band(song)
    print(lyrics)

    return lyrics # Return lyrics to web app.
