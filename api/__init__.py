import os

import flask_sqlalchemy
from dotenv import load_dotenv
from flask import Flask

db = flask_sqlalchemy.SQLAlchemy()


def create_app():
    load_dotenv()

    app = Flask(__name__)

    host = os.getenv('RDB_HOST')
    port = os.getenv('RDB_PORT')
    dbname = os.getenv('RDB_DBNAME')
    user = os.getenv('RDB_USER')
    password = os.getenv('RDB_PASSWORD')
    app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql+psycopg2://{user}:{password}@{host}:{port}/{dbname}'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.app_context().push()
    db.init_app(app)
    db.app = app
    db.create_all()

    from .api_v1 import api as api_v1
    app.register_blueprint(api_v1)

    return app
