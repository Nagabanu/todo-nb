"""Setup at app startup"""
from flask import Flask
import psycopg2



# def init_connection_engine():
#      app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Hr@7781@localhost:5432/postgres'
#      app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# conn = psycopg2.connect(
#         host="localhost",
#         database="postgres",
#         user="postgres",
#         password="Hr@7781")

# def get_db_connection():
#     psycopg2.connect(
#         host="localhost",
#         database="hr_portal",
#         user="postgres",
#         password="Hr@7781")


app = Flask(__name__)
# db = init_connection_engine()
# postgres = get_db_connection
postgres = psycopg2.connect(
        host="localhost",
        database="hr_portal",
        user="postgres",
        password="Hr@7781")
# To prevent from using a blueprint, we use a cyclic import
# This also means that we need to place this import here
# pylint: disable=cyclic-import, wrong-import-position
from app import routes
