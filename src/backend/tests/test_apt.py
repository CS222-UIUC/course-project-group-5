"""Test apt.py"""
from dataholders.apt import Apt


class TestApt:
    """Test Apt class"""

    sample_id = 0
    sample_name = "Sherman Hall"
    sample_address = "909 S 5th St"
    sample_rating = 3
    sample_price_min = 5500
    sample_price_max = 6500
    sample_apt = Apt(
        sample_id,
        sample_name,
        sample_address,
        sample_rating,
        sample_price_min,
        sample_price_max,
    )

    def test_name(self):
        """Test class stores correct name"""
        assert self.sample_name == self.sample_apt.name

    def test_address(self):
        """Test class stores correct address"""
        assert self.sample_address == self.sample_apt.address

    def test_rating(self):
        """Test class stores correct rating"""
        assert self.sample_rating == self.sample_apt.rating

    def test_price_min(self):
        """Test class stores correct min price"""
        assert self.sample_price_min == self.sample_apt.price_min

    def test_price_max(self):
        """Test class stores correct max price"""
        assert self.sample_price_max == self.sample_apt.price_max
