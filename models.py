from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey
from app import db


class Bands(db.Model):

    """ This table conatins all the bands the User favorites. """

    __tablename__ = 'fav_bands'

    id = db.Column('bandID', db.Integer, primary_key = True)
    band_name = db.Column(db.String(50))
    band_saved = db.Column(db.Boolean)

    def __init__(self,name,saved):

        self.band_name = name
        self.band_saved = saved
