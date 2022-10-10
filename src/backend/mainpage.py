"""Contains Main page class"""
from typing import List
from apt import Apt
from review import Review


class MainPage:
    """Mainpage class, interacts with the mainpage frontend"""

    def __init__(self) -> None:
        """Constructor"""
        # TODO: Implement in week 3

    def search_apartments(self, query: str) -> List[Apt]:
        """Returns a list of apartments with name matching query"""
        # TODO: Implement in week 3
        return []

    def apartments_default(self, num_apts: int) -> List[Apt]:
        """Returns num_apts apartments to populate the mainpage"""
        # TODO: Implement in week 3
        #       Apartments are sorted by default from most vote -> least vote
        return []

    def apartments_sorted(
        self, num_apts: int, price_sort: int, rating_sort: int
    ) -> List[Apt]:
        """Returns num_apts apartments with sorting criterias"""
        # TODO: Implement in week 3
        #       If both price_sort and rating_sort are selected,
        #       prioritize price_sort.
        #       If both are 0, then use apartments_default()'s behaviour.
        return []

    def get_apartments_pictures(self, apt_id: int) -> List[str]:
        """Returns pictures related to an apartment"""
        # TODO: Implement in week 3
        return []

    def get_apartments_reviews(self, apt_id: int) -> List[Review]:
        """Returns a list of apartment reviews"""
        # TODO: Implement in week 3
        return []
