import random
import requests
import json

from app.resource.album_cover import AlbumCover


class MakeSvg:
    def __init__(self):
        self.image = {}
        self.user = 'gabriel_ah'
        self.theme = 'light'
        self.style = 'default'
        self.time_refresh = '1500000000'

    def get_theme(self, select: str) -> dict:
        try:
            with open('app/templates/index.json', "r") as file:
                templates = json.load(file)
            return templates["themes"][select]
        except (KeyError, json.JSONDecodeError):
            print(f"Failed to load templates. Using default theme.")
            return templates["themes"]["light"]

    def get_style(self, select: str) -> dict:
        try:
            with open("app/templates/index.json", "r") as file:
                templates = json.load(file)
            return templates["style"][select]
        except (KeyError, json.JSONDecodeError):
            print(f"Failed to load templates. Using default style.")
            return templates["style"]["default"]

    def generate(self, data: list, theme_select: str, style_select: str, time_refresh: str) -> tuple:
        bar_count = 84
        content_bar = "".join([f"<div class='bar' style='left:{i*4}px; animation-duration:{random.randint(1000, 1350)}ms;'></div>" for i in range(bar_count)])
        album_cover = AlbumCover()

        theme = self.get_theme(theme_select)
        style = self.get_style(style_select)

        data_dict = {
            "contentBar": content_bar,
            "artistName": data["artist"]["#text"],
            "songName": data["name"],
            "songURI": data["url"],
            "image": album_cover.get_image(data["image"]),
            "backgroundColor": theme.get("color", {}).get("background", "#fff"),
            "songColor": theme.get("color", {}).get("song", "#000"),
            "artistColor": theme.get("color", {}).get("artist", "#000"),
            "timeRefresh": time_refresh
        }

        return style, data_dict
