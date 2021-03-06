from flask import Flask, request, flash, url_for, redirect, render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func, exists, and_
from datetime import *
from data_processing import *
from keys import *
from get_data import *


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///band_api_db.sqlite3'
app.config['SECRET_KEY'] = "roadie"

db = SQLAlchemy(app)
from models import *

google_key = keys['GOOGLE_KEY']


@app.route('/', methods = ['GET', 'POST'])
def home_page():


    if request.method == 'POST':

        band = request.form['artist']

        song = request.form['song'] # Song entry from user.


        if not band: # checks for a empty band string.

            if song and not band:

                lyrics = get_lyrics_for_song(song)

                return render_template('search_results.html', key = google_key, place = "guthrie+theater", state = "MN", song = lyrics)

            return render_template('home_page.html', key = google_key, place = "guthrie+theater", state = "MN")


        else:

            add_band_to_database(band) # program will save every band searched until deleted by User.  # Get APIs working first

            dates, photo = get_data_for_band(band)   # Use these in the template
            

            if not dates:

                not_found = "Sorry, that artist is not playing Minnesota at this time."

                return render_template('search_results.html', key = google_key, place = "guthrie+theater", state = "MN", artist_not_found = not_found, photos = photo)

            else:

                return render_template('search_results.html', key = google_key, place = dates[1], state = "MN", ticket_site = dates[0], photos = photo)


    return render_template('home_page.html', key = google_key, place = "guthrie+theater", state = "MN")


@app.route('/search_history', methods = ['GET','POST'])
def search_history():



    if request.method == 'POST':

        band = request.form['save_band']

        checked_query = request.form.getlist('query_artist')
        checked_delete = request.form.getlist('delete_artist')

        if len(checked_delete) == 1:

            delete_artist_from_db(band)

        elif len(checked_query) == 1: # Not the best work around, but saving photos to
                                      # a SQL database is really hard.

            song = '' # needed only becasue the method takes two variables

            dates, photo = get_data_for_band(band)   # Use these in the template

            if not dates:

                not_found = "Sorry, that artist is not playing Minnesota at this time."

                return render_template('search_results.html', key = google_key, place = "guthrie+theater", state = "MN", artist_not_found = not_found, photos = photo)

            else:

                return render_template('search_results.html', key = google_key, place = dates[1], state = "MN", ticket_site = dates[0], photos = photo)


        else:

            print("invalid input on checked boxes.") # This should flash to user.


    return render_template('search_history.html', band_list = Bands.query.all())

@app.route('/search_results')
def search_results():


    return render_template('search_results.html', key = google_key, place = "guthrie+theater", state = "MN")



def add_band_to_database(band):

    entry = Bands(band,False)

    db.session.add(entry)
    db.session.commit()

def delete_artist_from_db(band):

    query = Bands.query.filter_by(band_name = band).delete()

    db.session.commit()

if __name__ == '__main__':
    db.create_all()
    app.run(debug = True)
