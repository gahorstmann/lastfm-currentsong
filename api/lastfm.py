import os
import json
import random
import requests


from base64 import b64encode
from dotenv import load_dotenv, find_dotenv
from flask import Flask, Response, jsonify, render_template, templating, request

load_dotenv(find_dotenv())

LASTFM_TOKEN = os.getenv("LASTFM_TOKEN")

app = Flask(__name__)

def nowPlaying(user_lasftm):
    playing_url = "https://ws.audioscrobbler.com/2.0/?method=user.getrecenttracks&user={}&api_key={}&format=json&limit=1".format(user_lasftm, LASTFM_TOKEN)
    response = requests.get(playing_url)

    if response.status_code == 204:
        return {}
    return response.json()

def getTheme(theme_select):
    try:
        file = open("templates.json", "r")
        templates = json.loads(file.read())
        return templates["themes"][theme_select]
    except Exception as e:
        print(f"Failed to load templates.")
        return templates["themes"]["light"]

def getStyle(style_select):
    try:
        file = open("templates.json", "r")
        templates = json.loads(file.read())
        return templates["style"][style_select]
    except Exception as e:
        print(f"Failed to load templates.")
        return templates["style"]["default"]

def barGen(barCount):
    barCSS = ""
    left = 1
    for i in range(1, barCount + 1):
        anim = random.randint(1000, 1350)
        barCSS += (
            ".bar:nth-child({})  {{ left: {}px; animation-duration: {}ms; }}".format(
                i, left, anim
            )
        )
        left += 4
    return barCSS

def loadImageB64(url):
    response = requests.get(url)
    return b64encode(response.content).decode("ascii")

def makeSVG(data, theme_select, style_select, time_refresh):
    barCount = 84
    contentBar = "".join(["<div class='bar'></div>" for i in range(barCount)])
    barCSS = barGen(barCount)

    try:
        item = data["recenttracks"]["track"][0]
        image = loadImageB64(item["image"][3]["#text"])
        artistName = item["artist"]["#text"]
        songName = item["name"].replace("&", "&amp;")
        songURI = item["url"].replace("&", "&amp;")
    except Exception as e:
        image = loadImageB64("https://i.imgur.com/czRgoge.gif")
        artistName = "NaN"
        songName = "NaN"
        songURI = "https://github.com/apigamers/lastfm.currentsong"

    template = getTheme(theme_select)
    
    dataDict = {
        "contentBar": contentBar,
        "barCSS": barCSS,
        "artistName": artistName,
        "songName": songName,
        "songURI": songURI,
        "image": image,
        "backgroundColor": template["color"]["background"],
        "songColor": template["color"]["song"],
        "artistColor": template["color"]["artist"],
        "timeRefresh": time_refresh
    }

    return render_template(getStyle(style_select), **dataDict)

@app.route('/current', methods=['GET'])
def current():
    user_lasftm = request.args.get('user') or 'gabriel_ah'
    theme_select = request.args.get('theme') or 'light'
    style_select = request.args.get('style') or 'default'
    time_refresh = request.args.get('reload') or '1500000000'
    
    data = nowPlaying(user_lasftm)
    
    svg = makeSVG(data, theme_select, style_select, time_refresh)

    resp = Response(svg, mimetype="image/svg+xml")
    resp.headers["Cache-Control"] = "s-maxage=1"

    return resp

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=os.getenv("PORT") or 5000)
