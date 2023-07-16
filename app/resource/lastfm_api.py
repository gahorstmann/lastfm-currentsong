import requests
import json
import time

from app.enum.global_configs import SysConfigs
from app.enum.default_args import DefaultArgs
from app.models.current import CurrentModel

class LastFM:
    def __init__(self):
        self.api_key = SysConfigs.LASTFM_TOKEN.value
        self.base_url = SysConfigs.LASTFM_URL.value
        self.session = requests.Session()

    def get_current_track(self, user_id: str = DefaultArgs.USER_ID.value) -> CurrentModel:
        params = {
            'method': 'user.getrecenttracks',
            'user': user_id,
            'api_key': self.api_key,
            'format': 'json',
            'limit': 1,
        }
        response = self.session.get(self.base_url, params=params)
        response.raise_for_status()
        data = json.loads(response.text)
        if 'error' in data:
            raise ValueError(data['message'])

        return CurrentModel(user= user_id, 
                                  artist= data['recenttracks']['track'][0]['artist']['#text'],
                                  song= data['recenttracks']['track'][0]['name'],
                                  song_url = data['recenttracks']['track'][0]['url'],
                                  album = data['recenttracks']['track'][0]['album']['#text'],
                                  album_cover = data['recenttracks']['track'][0]['image'])
