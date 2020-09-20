from flask import Flask, jsonify
import os
from flask_sqlalchemy import SQLAlchemy
from waitress import serve


application = Flask(__name__)
application.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE']
application.config['SQLALCHEMY_TRACK_MODIFICATIONS']= False
db = SQLAlchemy(application)


class Error(Exception):
    def __init__(self, error, status_code):
        self.error = error
        self.status_code = status_code

# Database models
class Table(db.Model):
    __tablename__ = 'table'
    id = db.Column(db.Integer, primary_key=True)
    string = db.Column(db.String)
    datetime = db.Column(db.DateTime)
    integer = db.Column(db.Integer)

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def update(self):
        db.session.commit()


# URLs
@application.route('/')
def index():
    return "success"


@application.errorhandler(Error)
def error(error):
    return jsonify({
        "success": False,
        'error': error.status_code,
        "message": error.error,
        }), error.status_code


if __name__ == '__main__':
    application.run(host='0.0.0.0', port=8080, debug=True)
    # serve(application, port=80)