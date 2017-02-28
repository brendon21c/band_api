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

google_key = '' # We will need to secure this later.
TM_key = ''
url_test = ''

app = Flask(__name__)


@app.route('/', methods = ['GET', 'POST'])
def home_page():

    #photo_url = addPhotoToWebApp() # Getting a SSL cert fail on this.

    #get_band_tour_info(TM_key, 'norah jones')


    if request.method == 'POST':

        band = request.form['artist']

        URLS = ['https://app.ticketmaster.com/discovery/v2/events.json?apikey={}&keyword={}&stateCode=MN'.format(TM_key, band)
            ]

        return_list = concurrent_requests(URLS)
        print(return_list)

        if len(return_list) < 2:

            return render_template('home_page.html', key = google_key, place = "guthrie+theater", state = "MN", artist_not_found = return_list[0])

        else:

            return render_template('home_page.html', key = google_key, place = return_list[1], state = "MN", ticket_site = return_list[0])


    return render_template('home_page.html', key = google_key, place = "guthrie+theater", state = "MN")




def addPhotoToWebApp():# change pearl jam to a variable for whichever band the user inputs in the webapp

    '''I don't know how to add a photo to a web site using html newBPAPI.photo.url is a link to a photo,
    i hope that is something you can display using html. If not there is code that is commented out in
    bandPhotoAPI that can fetch the raw image from the url this code works but only after you quit the program'''


    newBPAPI = BandPhotoAPI('Pearl Jam')
    url = newBPAPI.photo.url
    print(url)

    return url



def setup():

    #url_test = addPhotoToWebApp()

    keyfile = open('keys.txt', 'r')

    global google_key # needed to assign keys to variables
    google_key = keyfile.readline().rstrip()
    print(google_key)

    global TM_key
    TM_key = keyfile.readline().rstrip()
    print(TM_key)

    keyfile.close()



if __name__ == '__main__':
    setup()
    app.run(debug = True)
