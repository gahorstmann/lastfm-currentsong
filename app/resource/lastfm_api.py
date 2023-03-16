import requests
import json
import time

class LastFM:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = 'https://ws.audioscrobbler.com/2.0/'

        # Cria um objeto Session do requests para reutilizar conexões HTTP
        self.session = requests.Session()

    def get_current_track(self, username) -> json:
        params = {
            'method': 'user.getrecenttracks',
            'user': username,
            'api_key': self.api_key,
            'format': 'json',
            'limit': 1,
        }
        response = self.session.get(self.base_url, params=params)
        
        # Verifica se houve um erro na solicitação
        response.raise_for_status()

        # Decodifica a resposta JSON
        data = json.loads(response.text)

        # Verifica se a solicitação foi bem-sucedida
        if 'error' in data:
            raise ValueError(data['message'])

        # Extrai a ultima música
        return data['recenttracks']['track'][0]
