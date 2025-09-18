import os
import sys
import json
import unittest

from unittest import mock

from flask import Flask
from flask_restful import Api

from app.models.current import CurrentModel
from app.enum.default_args import DefaultArgs
from app.resource.current_json import CurrentJson

HERE = os.path.dirname(os.path.abspath(__file__))
root_path = f'{HERE}/../../..'
sys.path.insert(0, root_path)

CREATE_JSON = {
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

    @mock.patch('app.resource.current_json.LastFM')
    def test_get_with_default_args(self, mock_last_fm):
        # Given
        mock_last_fm.return_value.get_current_track.return_value = CurrentModel(**CREATE_JSON)
        result_json = {
            'user': 'user',
            'artist': 'artist',
            'song': 'song',
            'song_url': 'song_url',
            'album': 'album',
            'album_cover': 'album_cover',
            'theme': DefaultArgs.THEME.value,
            'style': DefaultArgs.STYLE.value,
            'reload': DefaultArgs.RELOAD.value
        }
        
        # When
        response = self.client.get('/currentjson/user')

        # Then
        mock_last_fm.assert_called_once()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.text), result_json)
        
    @mock.patch('app.resource.current_json.LastFM')
    def test_get_with_custom_args(self, mock_last_fm):
        # Given
        mock_last_fm.return_value.get_current_track.return_value = CurrentModel(**CREATE_JSON)
        mock_last_fm.return_value.get_theme.return_value = THEME
        result_json = {
            'user': 'user',
            'artist': 'artist',
            'song': 'song',
            'song_url': 'song_url',
            'album': 'album',
            'album_cover': 'album_cover',
            'theme': THEME,
            'style': STYLE,
            'reload': DefaultArgs.RELOAD.value
        }

        # When
        response = self.client.get(f'/currentjson/user?theme={THEME}&style={STYLE}')

        # Then
        mock_last_fm.assert_called_once()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.text), result_json)
