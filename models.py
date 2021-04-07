from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)

database = "postgresql://xzruhowkodfply:c35a47e137e1ace774581beaee816314e152f72123e5c1cbe451694b931cb832@ec2-54-155-87-214.eu-west-1.compute.amazonaws.com:5432/dcj9v5e9cm8j0u"

app.config['SQLALCHEMY_DATABASE_URI'] = database
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= False
db = SQLAlchemy(app)

class Contacts(db.Model):
  __tablename__= "contacts"
  id = db.Column(db.Integer, primary_key=True)
  nom = db.Column(db.String)

  def insert(self):
    db.session.add(self)
    db.session.commit()

  def delete(self):
    db.session.delete(self)
    db.session.commit()

  def update(self):
    db.session.commit()


