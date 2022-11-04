"""Test review.py"""
from dataholders.review import Review


class TestReview:
    """Test Review class"""

    sample_username = "Minh Phan"
    sample_date = "2022-10-07"
    sample_comment = "Decent hall"
    sample_vote = True
    sample_review = Review(sample_username, sample_date, sample_comment, sample_vote)

    def test_username(self):
        """Test class stores correct username"""
        assert self.sample_username == self.sample_review.username

    def test_date(self):
        """Test class stores correct date"""
        assert self.sample_date == self.sample_review.date

    def test_comment(self):
        """Test class stores correct comment"""
        assert self.sample_comment == self.sample_review.comment

    def test_vote(self):
        """Test class stores correct vote"""
        assert self.sample_vote == self.sample_review.vote
