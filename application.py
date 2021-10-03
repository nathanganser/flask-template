from flask import Flask, jsonify
import os
from flask_sqlalchemy import SQLAlchemy
from waitress import serve
from dotenv import load_dotenv
from models import Contacts

load_dotenv()
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= False
db = SQLAlchemy(app)


class Error(Exception):
    def __init__(self, error, status_code):
        self.error = error
        self.status_code = status_code


# URLs
@app.route('/')
def index():
  age = 57
  return f"Ceci est le premier serveur de Antonio, qui a {age} ans"

@app.route('/contacts', methods=['GET', 'POST'])
def contacts():
  contacts = Contacts.query.all()
  return jsonify(contacts)




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
