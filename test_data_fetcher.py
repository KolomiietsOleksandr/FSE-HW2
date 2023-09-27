import unittest
from data_fetcher import CustomDataFetcher

class TestCustomDataFetcher(unittest.TestCase):
    def setUp(self):
        self.data_fetcher = CustomDataFetcher()

    def test_get_custom_data_from_url(self):
        custom_data = self.data_fetcher.get_custom_data_from_url("https://sef.podkolzin.consulting/api/users/lastSeen", 5)
        self.assertTrue(isinstance(custom_data, list))

if __name__ == '__main__':
    unittest.main()

#python3 -m unittest test_data_fetcher.py
