import unittest
from unittest.mock import patch
from url_shortener import shorten_url, expand_url
import validators

class TestUrlShortener(unittest.TestCase):

    @patch('url_shortener.pyshorteners.Shortener')
    def test_shorten_url(self, Shortener):
      
        eg_shortener = Shortener.return_value
        eg_shortener.tinyurl.short.return_value = 'http://short.url/123456'

        full_url = 'https://www.google.com'
        result = shorten_url(full_url)

        self.assertEqual(result, 'http://short.url/123456')
        eg_shortener.tinyurl.short.assert_called_once_with(full_url)

    @patch('url_shortener.pyshorteners.Shortener')
    def test_expand_url(self, Shortener):
        
        eg_shortener = Shortener.return_value
        eg_shortener.tinyurl.expand.return_value = 'https://www.google.com'

        short_url = 'http://short.url/123456'
        result = expand_url(short_url)

        self.assertEqual(result, 'https://www.google.com')
        eg_shortener.tinyurl.expand.assert_called_once_with(short_url)

    
    def test_is_URLValid(self):
        
        self.assertTrue(validators.url('https://www.google.com'))
        
        self.assertFalse(validators.url('htp://invalid-url'))

    
if __name__ == '__main__':
    unittest.main()