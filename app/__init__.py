import json
import pprint
import requests
from flask import Flask, request, jsonify
from .api.hello_world_routes import hello_world_routes
from .api.note_routes import note_routes
from .api.gpt_routes import gpt_routes
from os import path
from app.seeders.seeders import seed_note_data
from .models.models import Note
from .models.db import db


# db = SQLAlchemy()
DB_NAME = 'dev.db'


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
db.init_app(app)


# create blueprint to keep routes organized
app.register_blueprint(hello_world_routes, url_prefix='/api/hello')
app.register_blueprint(note_routes, url_prefix='/api/notes')
app.register_blueprint(gpt_routes, url_prefix='/api/gpt')


if not path.exists('instance/' + DB_NAME):
    with app.app_context():
        db.drop_all()
        db.create_all()  # Create all tables defined in models
        seed_note_data()
        print('seeding models succesffuly')
