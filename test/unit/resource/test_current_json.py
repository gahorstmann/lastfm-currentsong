import os
import sys
import unittest

from flask import Flask
from flask_restful import Api

from app.models.current import CurrentModel
from app.resource.current_json import CurrentJson

HERE = os.path.dirname(os.path.abspath(__file__))
root_path = f'{HERE}/../../..'
sys.path.insert(0, root_path)

TEST_JSON = {
    'user': 'user',
    'artist': 'artist',
    'song': 'song',
    'song_url': 'song_url',
    'album': 'album',
    'album_cover': 'album_cover'
}

THEME = 'dark'
STYLE = 'spotify'


class TestCurrentJson(unittest.TestCase):
    def setUp(self):
        self.app = Flask(__name__)
        self.api = Api(self.app)
        self.api.add_resource(CurrentJson, '/currentjson/<string:user_id>')
        self.client = self.app.test_client()

    def test_get_with_default_args(self, mock_last_fm):
        # Given
        mock_last_fm.return_value.get_current_track.return_value = CurrentModel(**TEST_JSON)
        
        # When
        response = self.client.get('/currentjson/user')
        
        # Then
        mock_last_fm.assert_called_once()
        self.assertEqual(response.status_code, 200)