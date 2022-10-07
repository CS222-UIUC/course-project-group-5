"""Test apt"""
from apt import Apt


class TestApt:
    """Test Apt class"""

    sample_name = "Sherman Hall"
    sample_address = "909 S 5th St"
    sample_rating = 3
    sample_price = (5500, 6500)
    sample_apt = Apt(sample_name, sample_address, sample_rating, sample_price)

    def test_name(self):
        """Test class stores correct name"""
        assert self.sample_name == self.sample_apt.get_name()

    def test_address(self):
        """Test class stores correct address"""
        assert self.sample_address == self.sample_apt.get_address()

    def test_rating(self):
        """Test class stores correct rating"""
        assert self.sample_rating == self.sample_apt.get_rating()

    def test_price_min(self):
        """Test class stores correct min price"""
        assert self.sample_price[0] == self.sample_apt.get_price_min()

    def test_price_max(self):
        """Test class stores correct max price"""
        assert self.sample_price[1] == self.sample_apt.get_price_max()
