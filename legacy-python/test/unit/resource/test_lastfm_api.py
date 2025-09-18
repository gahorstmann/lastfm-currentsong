import os
import sys
import unittest

from unittest import mock

from app.enum.default_args import DefaultArgs
from app.resource.lastfm_api import LastFM
from test.unit.model import HTTPResponse

HERE = os.path.dirname(os.path.abspath(__file__))
root_path = f'{HERE}/../../..'
sys.path.insert(0, root_path)

RESULT = {
    'user': 'user',
    'artist': 'artist',
    'song': 'song',
    'song_url': 'song_url',
    'album': 'album',
    'album_cover': [
        {
            "size": "small",
            "#text": "https://example.com/image.jpg"
        }
    ],
    'theme': DefaultArgs.THEME.value,
    'style': DefaultArgs.STYLE.value,
    'reload': DefaultArgs.RELOAD.value
}


class TestLastfmApi(unittest.TestCase):
    @mock.patch('requests.Session.get')
    def test_get_current_track_success(self, mock_request):
        # Given
        lastfm = LastFM()
        mock_value = HTTPResponse()
        mock_value.text = '''
        {
            "recenttracks": {
                "track": [
                {
                    "artist": {
                    "#text": "artist"
                    },
                        "image": [
                        {
                            "size": "small",
                            "#text": "https://example.com/image.jpg"
                        }
                        ],
                    "album": { "#text": "album" },
                    "name": "song",
                    "url": "song_url"
                }
                ]
            }
        }
        '''

        mock_request.return_value = mock_value

        # When
        result = lastfm.get_current_track('user')

        # Then
        self.assertEquals(result.json(), RESULT)

    @mock.patch('requests.Session.get')
    def test_get_current_track_error(self, mock_request):
        # Given
        lastfm = LastFM()
        mock_value = HTTPResponse()
        mock_value.text = '''
        {
            "error": "API Error Message",
            "message": "API Error Message"
        }
        '''
        mock_request.return_value = mock_value

        # When
        with self.assertRaises(ValueError) as cm:
            lastfm.get_current_track('user')
        
        print(cm.exception)
        # Then
        self.assertEqual(str(cm.exception), 'API Error Message')