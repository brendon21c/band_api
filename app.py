from flask import Flask, request, flash, url_for, redirect, render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func, exists, and_
import itertools
import json
import requests
import sys
import urllib.request
from datetime import *
from bandPhotoAPI import BandPhotoAPI
from photo import Photo
from tour_processing import *

google_key = 'AIzaSyAobnniB69jdRIJpi--eltsM1Z6tcPkqt4' # We will need to secure this later.
TM_key = 'xqbpUW8lmN8nnoX3UHO7suHosVMf8oBF'




app = Flask(__name__)


@app.route('/', methods = ['GET', 'POST'])
def home_page():

    #addPhotoToWebApp() TODO this will need to be tested, SSL fail.

    #get_band_schedule()

    band = "lil wayne"

    url = "https://app.ticketmaster.com/discovery/v2/events.json?apikey={}&keyword={}".format(TM_key, band)
    print(url)
    request_url = requests.get(url)
    json_return = request_url.json()
    json_1 = json.dumps(json_return)
    working = json.loads(json_1)
    json_value = working[0]
    print(json_value['events'])



    if request.method == 'POST':

        return render_template('home_page.html', key = google_key, place = request.form['venue'], state = request.form['state'])


    return render_template('home_page.html', key = google_key, place = "guthrie+theater", state = "MN", tour_key = TM_key, band_name = "lil wayne")



def addPhotoToWebApp():# change pearl jam to a variable for whichever band the user inputs in the webapp

    '''I don't know how to add a photo to a web site using html newBPAPI.photo.url is a link to a photo,
    i hope that is something you can display using html. If not there is code that is commented out in
    bandPhotoAPI that can fetch the raw image from the url this code works but only after you quit the program'''


    newBPAPI = BandPhotoAPI('Pearl Jam')
    print (newBPAPI.photo.url)

def get_band_tour_info(key, band):

    test_url = requests.get("https://app.ticketmaster.com/discovery/v2/events.json?apikey=%s&keyword=%s") (key,band)

    print(test_url)

if __name__ == '__main__':
    app.run(debug = True)
    addPhotoToWebApp()
