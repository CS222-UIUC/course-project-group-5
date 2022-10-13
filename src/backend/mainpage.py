"""Contains Main page class"""
import sqlite3
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
        query_sql = "%" + query + "%"
        connection = sqlite3.connect("database/database.db")
        cursor = connection.cursor()
        apt_query = cursor.execute(
            "SELECT apt_id, apt_name, apt_address, price_min, price_max \
            FROM Apartments WHERE apt_name LIKE ?", (query_sql,)
        ).fetchall()
        apts = []
        for entry in apt_query:
            rating_total = 0
            apt_id = int(entry[0])
            rating_query = cursor.execute(
                "SELECT vote FROM Ratings WHERE apt_id = ?", (apt_id,)
            ).fetchall()
            for rating in rating_query:
                if rating == 1:
                    rating_total += 1
                else:
                    rating_total -= 1
            apts.append(Apt(entry[0], entry[1], entry[2], rating_total, entry[3], entry[4]))
        connection.close()
        return apts

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
        connection = sqlite3.connect("database/database.db")
        cursor = connection.cursor()
        pic_query = cursor.execute(
            "SELECT link FROM AptPics WHERE apt_id = ?", (apt_id,)
        ).fetchall()
        res = []
        for entry in pic_query:
            res.append(entry[0])
        cursor.close()
        return res

    def get_apartments_reviews(self, apt_id: int) -> List[Review]:
        """Returns a list of apartment reviews"""
        # TODO: Implement in week 3
        connection = sqlite3.connect("database/database.db")
        cursor = connection.cursor()
        ratings_query = cursor.execute(
            "SELECT Users.username, Ratings.date_of_rating, Ratings.comment, Ratings.vote \
            FROM Users, Ratings WHERE Users.user_id = Ratings.user_id"
        ).fetchall()
        reviews = []
        for entry in ratings_query:
            reviews.append(Review(entry[0], entry[1], entry[2], entry[3]))
        cursor.close()
        return reviews
