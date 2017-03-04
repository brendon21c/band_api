from flask import Flask, request, flash, url_for, redirect, render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func, exists, and_
import itertools
import json
import requests
import sys
import urllib.request
from datetime import *
from data_processing import *
from keys import *
from get_data import get_data_for_band


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///band_api_db.sqlite3'
app.config['SECRET_KEY'] = "roadie"

db = SQLAlchemy(app)
from models import *

google_key = keys['GOOGLE_KEY']


@app.route('/', methods = ['GET', 'POST'])
def home_page():

    #photo_url = addPhotoToWebApp() # Getting a SSL cert fail on this.

    #get_band_tour_info(TM_key, 'norah jones')

    if request.method == 'POST':

        band = request.form['artist']

        add_band_to_database(band) # program will save every band searched until deleted by User.  # Get APIs working first

        dates, photo, lyrics = get_data_for_band(band)   # Use these in the template

        if not dates:

            not_found = "Sorry, that artist is not playing Minnesota at this time."

            return render_template('home_page.html', key = google_key, place = "guthrie+theater", state = "MN", artist_not_found = not_found)

        else:

            return render_template('home_page.html', key = google_key, place = dates[1], state = "MN", ticket_site = dates[0], photo_url = photo)


    return render_template('home_page.html', key = google_key, place = "guthrie+theater", state = "MN")


@app.route('/search_history', methods = ['GET','POST'])
def search_history():



    if request.method == 'POST':

        band = request.form['save_band']

        checked_save = request.form.getlist('save_artist')
        checked_delete = request.form.getlist('delete_artist')

        print(len(checked_save))

        if len(checked_delete) == 1:

            delete_artist_from_db(band)

        elif len(checked_save) == 1:

            print(checked_save[0])

        else:

            print("invalid input on checked boxes.") # This should flash to user.

        # if len(checked2) == 1:
        #
        #     delete_artist_from_db(band)

    return render_template('search_history.html', band_list = Bands.query.all())


def add_band_to_database(band):

    entry = Bands(band,False)

    db.session.add(entry)
    db.session.commit()

def delete_artist_from_db(band):

    query = Bands.query.filter_by(band_name = band).delete()



if __name__ == '__main__':
    db.create_all()
    app.run(debug = True)
