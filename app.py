from flask import Flask, request, flash, url_for, redirect, render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func, exists, and_
import itertools
import json
import requests
import sys
import urllib.request
from datetime import *
from bandPhotoAPI import *
from photo import Photo
from data_processing import *

google_key = 'AIzaSyAobnniB69jdRIJpi--eltsM1Z6tcPkqt4' # We will need to secure this later.
TM_key = 'xqbpUW8lmN8nnoX3UHO7suHosVMf8oBF'


app = Flask(__name__)


@app.route('/', methods = ['GET', 'POST'])
def home_page():

    #photo_url = addPhotoToWebApp() # Getting a SSL cert fail on this.

    #get_band_tour_info(TM_key, 'norah jones')

    if request.method == 'POST':

        band = request.form['artist']

        URLS = ['https://app.ticketmaster.com/discovery/v2/events.json?apikey={}&keyword={}'.format(TM_key, band)
            ]

        return_list = concurrent_requests(URLS)

        return render_template('home_page.html', key = google_key, place = return_list[1], state = request.form['state'])


    return render_template('home_page.html', key = google_key, place = "guthrie+theater", state = "MN", tour_key = TM_key, band_name = "lil wayne")



def addPhotoToWebApp():# change pearl jam to a variable for whichever band the user inputs in the webapp

    '''I don't know how to add a photo to a web site using html newBPAPI.photo.url is a link to a photo,
    i hope that is something you can display using html. If not there is code that is commented out in
    bandPhotoAPI that can fetch the raw image from the url this code works but only after you quit the program'''


    newBPAPI = BandPhotoAPI('Pearl Jam')
    url = newBPAPI.photo.url
    print(url)

    return url




def get_band_tour_info(key, band):

    url = "https://app.ticketmaster.com/discovery/v2/events.json?apikey={}&keyword={}".format(key, band)
    print(url)
    request_url = requests.get(url)
    json_return = request_url.json() # TODO need to get specific information from here.

    print(type(json_return))
    artist = json_return["_embedded"]['events'] # Gets Artist
    print(type(artist))
    print(len(artist))
    # venue = artist["_embedded"]['venues'] # Gets venue
    # print(type(venue))
    # print(len(venue))


if __name__ == '__main__':
    app.run(debug = True)
    addPhotoToWebApp()
