from keys import keys
from ticketmaster import *
from band_images import *
from lyrics import *


def get_data_for_band(band):

    # At the moment, make three requests, one after the other
    # Future: make all three request concurrently
    # Future: check cache for info before making requests

    # todo get data from ticketmaster. Return data in suitable format for template 
    ticketmaster_data = ticketmaster.get_data_for_band(band)

    # todo get data from image source Return data in suitable format for template
    photos = band_images.get_photos_for_band(band)

    # todo get lyrics. Return data in suitable format for template
    lyrics = lyrics.get_lyrics_for_band(band)

    # return all data in suitable form for using in template.

    return ticketmaster_data, photos, lyrics
