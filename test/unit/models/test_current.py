import os
import sys
import unittest

from app.models.current import CurrentModel
from app.enum.default_args import DefaultArgs

HERE = os.path.dirname(os.path.abspath(__file__))
root_path = f'{HERE}/../../..'
sys.path.insert(0, root_path)

DEFAULT_JSON = {
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

THEME = 'dark'
STYLE = 'spotify'
RELOAD = 10000000


class TestModelCurrent(unittest.TestCase):
    def test_json_current(self):
        # Given
        mock_current = CurrentModel('user', 'artist', 'song', 'song_url', 'album', 'album_cover')
        
        # When
        result = mock_current.json()
        
        # Then
        self.assertEqual(result, DEFAULT_JSON)

    def test_set_theme(self):
        # Given
        mock_current = CurrentModel('user', 'artist', 'song', 'song_url', 'album', 'album_cover')
        
        # When
        mock_current.set_theme(THEME)
        result = mock_current.json().get('theme')
        
        # Then
        self.assertEqual(result, THEME)
        
    def test_set_style(self):
        # Given
        mock_current = CurrentModel('user', 'artist', 'song', 'song_url', 'album', 'album_cover')
        
        # When
        mock_current.set_style(STYLE)
        result = mock_current.json().get('style')
        
        # Then
        self.assertEqual(result, STYLE)
        
    
    def test_set_reload(self):
        # Given
        mock_current = CurrentModel('user', 'artist', 'song', 'song_url', 'album', 'album_cover')
        
        # When
        mock_current.set_reload(RELOAD)
        result = mock_current.json().get('reload')
        
        # Then
        self.assertEqual(result, RELOAD)