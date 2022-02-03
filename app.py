from flask import Flask, render_template, redirect, request, flash
from flask_sqlalchemy import SQLAlchemy
import requests

app = Flask (__name__)
app.config ['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.sqlite3'
db = SQLAlchemy(app)

@app.route("/")
def index():
    response = requests.get("https://api.twitchfa.com/v2/twitch/streamers?page=1&limit=25")
    streamers = []
    views = []
    games = []
    thumbnails = []
    ids = []
    for i in range(25):
        streamers.append(response.json()['data'][i]['displayName'])
        views.append(response.json()['data'][i]['viewers'])
        games.append(response.json()['data'][i]['gameName'])
        thumbnails.append(response.json()['data'][i]['profileUrl'])
        ids.append(response.json()['data'][i]['login'])
    return render_template("index.html", streamers= streamers, views= views, games= games, thumbnails= thumbnails, ids= ids)