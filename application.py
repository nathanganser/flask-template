from flask import Flask, jsonify, request
import os
from flask_sqlalchemy import SQLAlchemy
from waitress import serve
from dotenv import load_dotenv
from models import Contacts, app

load_dotenv()



class Error(Exception):
    def __init__(self, error, status_code):
        self.error = error
        self.status_code = status_code


# URLs
@app.route('/')
def index():
  age = 25
  return f"Ceci est le premier serveur de Nathan, qui a {age} ans"

@app.route('/contacts', methods=['GET', 'POST'])
def contacts():
  contacts = Contacts.query.all()
  json = {}
  for contact in contacts:
    json[contact.id] = contact.nom

  return jsonify(json)

@app.route('/contact/<id>')
def contact(id):
  contact = Contacts.query.filter_by(id=id).first()
  return jsonify(id=contact.id, nom=contact.nom)

@app.route('/contact', methods=['POST', 'DELETE'])
def create_or_delete_contact():
  data = request.json
  nom = data.get('nom')

  if request.method == 'POST':
    
    contact = Contacts(nom=nom)
    contact.insert()
    return jsonify(message="Contact créé!")
  elif request.method == 'DELETE':
    contact = Contacts.query.filter_by(nom=nom).first()
    contact.delete()
    return jsonify(message="Contact supprimé")




@app.errorhandler(Error)
def error(error):
    return jsonify({
        "success": False,
        'error': error.status_code,
        "message": error.error,
    }), error.status_code


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
    # serve(app, port=80)
