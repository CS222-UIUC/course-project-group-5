"""Contains Apartment class"""
from typing import Tuple

class Apt:
    """Apt class, stores detail about an apartment"""

    def __init__(self, name:str, address: str, rating: int, price: Tuple[int, int]) -> None:
        """Constructor"""
        # TODO: Implement in week 3
        #       The first argument of the tuple is the min price
        #       The second argument is the max price
        #       Have to group them in a tuple to satisfy the pylint god

    def get_name(self) -> str:
        """Returns name of apartment"""
        # TODO: Implement in week 3

    def get_address(self) -> str:
        """Returns address of apartment"""
        # TODO: Implement in week 3

    def get_rating(self) -> int:
        """Returns rating of apartment"""
        # TODO: Implement in week 3
        #       Formula: total_upvote - total_downvote

    def get_price_max(self) -> int:
        """Returns maximum price of apartment"""
        # TODO: Implement in week 3

    def get_price_min(self) -> int:
        """Returns minimum price of apartment"""
        # TODO: Implement in week 3
        