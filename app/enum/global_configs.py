import os

from enum import Enum


class SysConfigs(Enum):
    HOST = os.getenv('HOST')
    PORT = os.getenv('PORT')
    LASTFM_URL = 'https://ws.audioscrobbler.com/2.0/'
    LASTFM_TOKEN = os.getenv('LASTFM_TOKEN')
    TEMPLATE_INDEX = 'app/templates/index.json'
