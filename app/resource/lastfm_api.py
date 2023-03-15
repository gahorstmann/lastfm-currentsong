import requests
import json
import time

class LastFM:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = 'https://ws.audioscrobbler.com/2.0/'

        # Cria um objeto Session do requests para reutilizar conexões HTTP
        self.session = requests.Session()

    def get_current_track(self, username, image_size):
        """
        Retorna a música atual do usuário.
        """
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

        print(data)

        # Verifica se a solicitação foi bem-sucedida
        if 'error' in data:
            raise ValueError(data['message'])

        # Extrai informações relevantes da resposta
        track = data['recenttracks']['track'][0]['name']
        artist = data['recenttracks']['track'][0]['artist']['#text']
        album = data['recenttracks']['track'][0]['album']['#text']
        image = data['recenttracks']['track'][0]["image"][image_size]["#text"]
        
        return track, artist, album, image
