from flask import Flask, request, flash, url_for, redirect, render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func, exists, and_
import itertools
from datetime import *

google_key = 'AIzaSyAobnniB69jdRIJpi--eltsM1Z6tcPkqt4' # We will need to secure this later.
TM_key = 'xqbpUW8lmN8nnoX3UHO7suHosVMf8oBF'




app = Flask(__name__)


@app.route('/', methods = ['GET', 'POST'])
def home_page():

    if request.method == 'POST':

        return render_template('home_page.html', key = google_key, place = request.form['venue'], state = request.form['state'])


    return render_template('home_page.html', key = google_key, place = "guthrie+theater", state = "MN")


if __name__ == '__main__':
    app.run(debug = True)
