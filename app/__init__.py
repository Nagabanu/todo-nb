"""Setup at app startup"""
from flask import Flask
import psycopg2


app = Flask(__name__)
postgres = psycopg2.connect(
        host="dpg-cepqpmhgp3jlcslol9ig-a.oregon-postgres.render.com",
        database="todo_kp05",
        user="root",
        password="Kr2GQVqkwjZ6fYNwDBLenJrX6Bwiz4pN")
# To prevent from using a blueprint, we use a cyclic import
# This also means that we need to place this import here
# pylint: disable=cyclic-import, wrong-import-position
from app import routes
