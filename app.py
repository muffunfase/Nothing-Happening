from flask import render_template
from db import create_app, db


app=create_app()

app.secret_key = 'fefefe'

@app.route('/')
def index():
    return render_template('home.html', page='home')

@app.route('/about')
def about_page():
    return render_template('about.html', page='about')

@app.route('/uh')
def other_page():
    return render_template('other.html', page='other')