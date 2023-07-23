import random
import json

from app.enum.global_configs import SysConfigs
from app.enum.default_args import DefaultArgs
from app.enum.messages import Messages
from app.util.converter.album_cover import get_image


class MakeSVG:
    def __init__(self):
        self.template_index = SysConfigs.TEMPLATE_INDEX.value

    def get_theme(self, select: str) -> dict:
        try:
            with open(self.template_index, "r") as file:
                templates = json.load(file)
            return templates["themes"][select]
        except (KeyError, json.JSONDecodeError):
            print(Messages.FAILED_LOAD_TEMPLATES.value)
            return templates["themes"][DefaultArgs.THEME.value]

    def get_style(self, select: str) -> dict:
        try:
            with open(self.template_index, "r") as file:
                templates = json.load(file)
            return templates["style"][select]
        except (KeyError, json.JSONDecodeError):
            print(Messages.FAILED_LOAD_TEMPLATES.value)
            return templates["style"][DefaultArgs.STYLE.value]
        
    def replace_char(self, data) -> str:
        result = data.replace("&","&amp;")
        return result

    def generate(self, data: json) -> tuple:
        bar_count = 84
        content_bar = "".join([f"<div class='bar' style='left:{i*4}px; animation-duration:{random.randint(1000, 1350)}ms;'></div>" for i in range(bar_count)])

        theme = self.get_theme(data.get("theme"))
        style = self.get_style(data.get("style"))

        data_dict = {
            "contentBar": content_bar,
            "artistName": self.replace_char(data.get("artist")),
            "songName": self.replace_char(data.get("song")),
            "image": get_image(data.get("album_cover")),
            "backgroundColor": theme.get("color", {}).get("background", "#fff"),
            "songColor": theme.get("color", {}).get("song", "#000"),
            "artistColor": theme.get("color", {}).get("artist", "#000"),
            "timeRefresh": data.get("reload")
        }

        return style, data_dict
