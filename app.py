from os import environ, getenv, scandir
from flask import render_template
from db import create_app, db


app=create_app()

app.secret_key = 'fefefe'

@app.route('/')
def index():
    return render_template('home.html')