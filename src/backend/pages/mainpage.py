"""Contains Main page class"""
import sqlite3
from datetime import date
from typing import List
from typing import Tuple
from dataholders.apt import Apt
from dataholders.review import Review
from decorators import use_database

class MainPage:
    """Mainpage class, interacts with the mainpage frontend"""

    def __init__(self) -> None:
        """Constructor"""

    @use_database
    def search_apartments(self, query: str) -> List[Apt]:
        """Returns a list of apartments with name matching query"""
        query_sql = "%" + query.lower() + "%"
        apt_query = self.search_apartments.cursor.execute(
            "SELECT Apartments.apt_id, Apartments.apt_name, Apartments.apt_address, \
            COALESCE(SUM(Reviews.vote), 0) AS 'total_vote', \
            Apartments.price_min, Apartments.price_max \
            FROM Apartments LEFT JOIN Reviews ON Apartments.apt_id = Reviews.apt_id \
            WHERE LOWER(Apartments.apt_name) LIKE ? \
            GROUP BY Apartments.apt_id",
            (query_sql,),
        ).fetchall()
        apts = []
        for entry in apt_query:
            if entry[0] is not None:
                apts.append(
                    Apt(entry[0], entry[1], entry[2], entry[3], entry[4], entry[5])
                )
        return apts

    @use_database
    def apartments_default(self, num_apts: int) -> List[Apt]:
        """Returns num_apts apartments to populate the mainpage"""
        apt_query = self.apartments_default.cursor.execute(
            "SELECT Apartments.apt_id, Apartments.apt_name, Apartments.apt_address, \
            COALESCE(SUM(Reviews.vote), 0) AS 'total_vote', \
            Apartments.price_min, Apartments.price_max \
            FROM Apartments LEFT JOIN Reviews ON Apartments.apt_id = Reviews.apt_id \
            GROUP BY Apartments.apt_id \
            ORDER BY total_vote DESC, Apartments.apt_name LIMIT ?",
            (num_apts,),
        ).fetchall()
        apts = []
        for entry in apt_query:
            apts.append(Apt(entry[0], entry[1], entry[2], entry[3], entry[4], entry[5]))
        return apts

    @use_database
    def apartments_sorted(
        self, num_apts: int, price_sort: int, rating_sort: int
    ) -> List[Apt]:
        """Returns num_apts apartments with sorting criterias"""

        apts = []
        apt_query = []

        if price_sort == 0:
            apt_query = self.rating_sort_helper(num_apts, rating_sort, self.apartments_sorted.cursor)
        elif rating_sort == 0 and price_sort != 0:
            apt_query = self.price_sort_helper(num_apts, price_sort, self.apartments_sorted.cursor)
        else:
            apt_query = self.both_sort_helper(num_apts, price_sort, rating_sort, self.apartments_sorted.cursor)

        for entry in apt_query:
            apts.append(Apt(entry[0], entry[1], entry[2], entry[3], entry[4], entry[5]))
        return apts

    def rating_sort_helper(
        self, num_apts: int, rating_sort: int, cursor: sqlite3.Cursor
    ) -> List[Tuple]:
        """Helper for rating-only sort"""
        rating_order = ""
        if rating_sort in (0, 1):
            rating_order = "DESC"
        apt_query = cursor.execute(
            f"SELECT Apartments.apt_id, Apartments.apt_name, Apartments.apt_address, \
            COALESCE(SUM(Reviews.vote), 0) AS 'total_vote', \
            Apartments.price_min, Apartments.price_max \
            FROM Apartments LEFT JOIN Reviews ON Apartments.apt_id = Reviews.apt_id \
            GROUP BY Apartments.apt_id \
            ORDER BY total_vote {rating_order}, \
            Apartments.apt_name \
            LIMIT ?",
            (num_apts,),
        ).fetchall()

        return apt_query

    def price_sort_helper(
        self, num_apts: int, price_sort: int, cursor: sqlite3.Cursor
    ) -> List[Tuple]:
        """Helper for price-only sorts"""
        price_order = ""
        if price_sort == 1:
            price_order = "DESC"
        apt_query = cursor.execute(
            f"SELECT Apartments.apt_id, Apartments.apt_name, Apartments.apt_address, \
            COALESCE(SUM(Reviews.vote), 0) AS 'total_vote', \
            Apartments.price_min, Apartments.price_max \
            FROM Apartments LEFT JOIN Reviews ON Apartments.apt_id = Reviews.apt_id \
            GROUP BY Apartments.apt_id \
            ORDER BY (Apartments.price_min + Apartments.price_max)/2 {price_order}, \
            Apartments.apt_name \
            LIMIT ?",
            (num_apts,),
        ).fetchall()

        return apt_query

    def both_sort_helper(
        self, num_apts: int, price_sort: int, rating_sort: int, cursor: sqlite3.Cursor
    ) -> List[Tuple]:
        """Helper to sort both params"""

        price_order = ""
        if price_sort == 1:
            price_order = "DESC"
        rating_order = ""
        if rating_sort == 1:
            rating_order = "DESC"

        apt_query = cursor.execute(
            f"SELECT Apartments.apt_id, Apartments.apt_name, Apartments.apt_address, \
            COALESCE(SUM(Reviews.vote), 0) AS 'total_vote', \
            Apartments.price_min, Apartments.price_max \
            FROM Apartments LEFT JOIN Reviews ON Apartments.apt_id = Reviews.apt_id \
            GROUP BY Apartments.apt_id \
            ORDER BY (Apartments.price_min + Apartments.price_max)/2 {price_order}, \
            total_vote {rating_order}, \
            Apartments.apt_name \
            LIMIT ?",
            (num_apts,),
        ).fetchall()

        return apt_query

    @use_database
    def get_apartments_pictures(self, apt_id: int) -> List[str]:
        """Returns pictures related to an apartment"""
        pic_query = self.get_apartments_pictures.cursor.execute(
            "SELECT link FROM AptPics WHERE apt_id = ?", (apt_id,)
        ).fetchall()
        res = []
        for entry in pic_query:
            res.append(entry[0])
        return res

    @use_database
    def write_apartment_review(
        self, apt_id: int, username: str, comment: str, vote: int
    ) -> List[Review]:
        """Write a new review for apartment"""
        user_id = self.write_apartment_review.cursor.execute(
            "SELECT user_id FROM Users WHERE username = ?", (username,)
        ).fetchone()[0]
        today = date.today().strftime("%Y-%m-%d")
        self.write_apartment_review.cursor.execute(
            "INSERT INTO Reviews (apt_id, user_id, date_of_rating, comment, vote) \
            VALUES (?, ?, ?, ?, ?) \
            ON CONFLICT DO UPDATE SET \
                date_of_rating = excluded.date_of_rating, \
                comment = excluded.comment, \
                vote = excluded.vote",
            (apt_id, user_id, today, comment, vote),
        )
        self.write_apartment_review.connection.commit()

        ratings_query = self.write_apartment_review.cursor.execute(
            "SELECT Users.username, Reviews.date_of_rating, Reviews.comment, Reviews.vote \
            FROM Users INNER JOIN Reviews \
            ON Users.user_id = Reviews.user_id \
            WHERE Reviews.apt_id = ? \
            ORDER BY Users.username = ? DESC, Reviews.date_of_rating DESC",
            (apt_id, username),
        ).fetchall()
        return self.create_reviews_helper(ratings_query)

    @use_database
    def get_apartments_reviews(self, apt_id: int) -> List[Review]:
        """Returns a list of apartment reviews"""
        ratings_query = self.get_apartments_reviews.cursor.execute(
            "SELECT Users.username, Reviews.date_of_rating, Reviews.comment, Reviews.vote \
            FROM Users INNER JOIN Reviews \
            ON Users.user_id = Reviews.user_id \
            WHERE Reviews.apt_id = ? \
            ORDER BY Reviews.date_of_rating DESC",
            (apt_id,),
        ).fetchall()
        return self.create_reviews_helper(ratings_query)

    def create_reviews_helper(self, ratings_query: List[Tuple]) -> List[Review]:
        reviews = []
        for entry in ratings_query:
            if entry[0] is not None:
                vote = False
                if entry[3] == 1:
                    vote = True
                reviews.append(Review(entry[0], entry[1], entry[2], vote))
        return reviews
