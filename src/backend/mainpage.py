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
            "SELECT Apartments.apt_id, Apartments.apt_name, Apartments.apt_address, \
            COALESCE(SUM(Reviews.vote), 0), Apartments.price_min, Apartments.price_max \
            FROM Apartments, Reviews WHERE Apartments.apt_name LIKE ? \
            AND Apartments.apt_id = Reviews.apt_id",
            (query_sql,),
        ).fetchall()
        apts = []
        for entry in apt_query:
            apts.append(Apt(entry[0], entry[1], entry[2], entry[3], entry[4], entry[5]))
        connection.close()
        return apts

    def apartments_default(self, num_apts: int) -> List[Apt]:
        """Returns num_apts apartments to populate the mainpage"""
        connection = sqlite3.connect("database/database.db")
        cursor = connection.cursor()
        apt_query = cursor.execute(
            "SELECT Apartments.apt_id, Apartments.apt_name, Apartments.apt_address, \
            COALESCE(SUM(Reviews.vote), 0) AS 'total_vote', \
            Apartments.price_min, Apartments.price_max \
            FROM Apartments LEFT JOIN Reviews ON Apartments.apt_id = Reviews.apt_id \
            GROUP BY Apartments.apt_id \
            ORDER BY total_vote DESC, Apartments.apt_name LIMIT ?",
            (num_apts,),
        ).fetchall()
        print(apt_query)
        apts = []
        for entry in apt_query:
            apts.append(Apt(entry[0], entry[1], entry[2], entry[3], entry[4], entry[5]))
        connection.close()
        return apts

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
            "SELECT Users.username, Reviews.date_of_rating, Reviews.comment, Reviews.vote \
            FROM Users, Reviews WHERE Users.user_id = Reviews.user_id AND Reviews.apt_id = ?",
            (apt_id,),
        ).fetchall()
        reviews = []
        for entry in ratings_query:
            vote = False
            if entry[3] == 1:
                vote = True
            reviews.append(Review(entry[0], entry[1], entry[2], vote))
        cursor.close()
        return reviews
