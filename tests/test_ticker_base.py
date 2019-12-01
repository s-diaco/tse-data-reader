import unittest

from tesreader.ticker_base import TickerBase


class TestTickerBase(unittest.TestCase):
    def setUp(self):
        self.ticker_base = TickerBase("فخوز")

    def test_get_id(self):
        id = self.ticker_base.get_id()
        self.assertEqual(id, 28864540805361867)

    def test_info(self):
        self.ticker_base._get_info()


