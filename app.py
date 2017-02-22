from flask import Flask, request, flash, url_for, redirect, render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func, exists, and_
import itertools
from datetime import *
from bandPhotoAPI import BandPhotoAPI
from photo import Photo

google_key = 'AIzaSyAobnniB69jdRIJpi--eltsM1Z6tcPkqt4' # We will need to secure this later.


app = Flask(__name__)


@app.route('/', methods = ['GET', 'POST'])
def home_page():

    if request.method == 'POST':

        return render_template('home_page.html', key = google_key, place = request.form['venue'], state = request.form['state'])


    return render_template('home_page.html', key = google_key, place = "guthrie+theater", state = "MN")
''' I don't know how to add a photo to a web site using html newBPAPI.photo.url is a link to a photo,
    i hope that is something you can display using html. If not there is code that is commented out in
    bandPhotoAPI that can fetch the raw image from the url'''
'''this code works but only after you quit the program'''
def addPhotoToWebApp()# change pearl jam to a variable for whichever band the user inputs in the webapp
    newBPAPI = BandPhotoAPI('Pearl Jam')
    print (newBPAPI.photo.url)


if __name__ == '__main__':
    app.run(debug = True)
    addPhotoToWebApp()
