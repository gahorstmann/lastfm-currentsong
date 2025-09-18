import os

from enum import Enum


class SysConfigs(Enum):
    HOST = os.getenv('HOST', '0.0.0.0')
    PORT = os.getenv('PORT', '8080')
    LASTFM_URL = 'https://ws.audioscrobbler.com/2.0/'
    LASTFM_TOKEN = os.getenv('LASTFM_TOKEN')
    TEMPLATE_INDEX = 'app/templates/index.json'
