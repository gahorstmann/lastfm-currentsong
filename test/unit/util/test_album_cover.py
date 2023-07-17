import os
import sys
import unittest

from unittest import mock

from app.util.converter.album_cover import get_image_lastfm
from test.unit.model import HTTPResponse

HERE = os.path.dirname(os.path.abspath(__file__))
root_path = f'{HERE}/../../..'
sys.path.insert(0, root_path)


class TestAlbumCover(unittest.TestCase):
    @mock.patch('request.get')
    def get_image_lastfm(self, mock_request):
        # Given
        mock_request.return_value = HTTPResponse()
        
        # When
        result = get_image_lastfm('http://example.com')
        
        # Then
        mock_request.assert_called_once()
        self.assertEqual(result, '')