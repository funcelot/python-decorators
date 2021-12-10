# pylint:disable=unnecessary-pass,wrong-import-position
""" Tests """
import unittest
from datetime import datetime
from unittest.mock import patch

from datetime_service import get_datetime


@patch("datetime_service.datetime")
def test_get_datetime(mock_datetime):
    """Method test"""
    expected = datetime.strptime("2020-12-31 23:59:59", "%Y-%m-%d %H:%M:%S")
    mock_datetime.now = lambda: expected
    actual = get_datetime()
    assert actual == expected


class TestDefault(unittest.TestCase):
    """Default methods tests"""

    @patch("datetime_service.datetime")
    def test_get_datetime(self, mock_datetime):
        """Method test"""
        expected = datetime.strptime("2021-01-01 00:00:00", "%Y-%m-%d %H:%M:%S")
        mock_datetime.now = lambda: expected
        actual = get_datetime()
        assert actual == expected


if __name__ == "__main__":
    unittest.main()
