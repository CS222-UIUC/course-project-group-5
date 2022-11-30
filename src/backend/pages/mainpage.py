"""Contains Main page class"""
from datetime import date
from typing import List
from typing import Tuple
from dataclasses import dataclass
from dataholders.apt import Apt
from dataholders.review import Review
from decorators import use_database


@dataclass(frozen=True)
class LatestPopulatedApt:
    """Stores details related to the latest apt in a scroll"""

    apt_name: str
    apt_id: int


class MainPage:
    """Mainpage class, interacts with the mainpage frontend"""

    populate_query = "WITH temp(id, name, address, total_vote, p_min, p_max, p_avg) AS \
    (SELECT Apartments.apt_id, Apartments.apt_name, Apartments.apt_address, \
    COALESCE(SUM(Reviews.vote), 0), \
    Apartments.price_min, Apartments.price_max, \
    (Apartments.price_min + Apartments.price_max)/2 \
    FROM Apartments LEFT JOIN Reviews ON Apartments.apt_id = Reviews.apt_id \
    GROUP BY Apartments.apt_id) "

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
    def populate_apartments(
        self, num_apts: int, price_sort: int, rating_sort: int, apt_id: int
    ) -> List[Apt]:
        """Returns num_apts apartments with sorting criterias"""

        apts = []
        apt_query = []

        apt_name = ""
        if apt_id >= 0:
            apt_name = self.populate_apartments.cursor.execute(
                "SELECT apt_name FROM Apartments WHERE apt_id = ?", (apt_id,)
            ).fetchone()[0]
        latest_row = LatestPopulatedApt(apt_name, apt_id)
        if price_sort == 0:
            apt_query = self.rating_sort_helper(num_apts, rating_sort, latest_row)
        elif rating_sort == 0 and price_sort != 0:
            apt_query = self.price_sort_helper(num_apts, price_sort, latest_row)
        else:
            apt_query = self.both_sort_helper(
                num_apts, price_sort, rating_sort, latest_row
            )

        for entry in apt_query:
            apts.append(Apt(entry[0], entry[1], entry[2], entry[3], entry[4], entry[5]))
        return apts

    @use_database
    def rating_sort_helper(
        self, num_apts: int, rating_sort: int, latest_row: LatestPopulatedApt
    ) -> List[Tuple]:
        """Helper for rating-only sort"""
        rating_order = "DESC" if rating_sort in (0, 1) else ""
        rating_comp = "<" if rating_sort in (0, 1) else ">"
        apt_query = []
        if latest_row.apt_id >= 0:
            apt_query = self.rating_sort_helper.cursor.execute(
                self.populate_query
                + f"SELECT * FROM temp \
                WHERE \
                (total_vote = (SELECT total_vote FROM temp WHERE id = ?) \
                AND (name, id) > (?, ?)) \
                OR total_vote {rating_comp} (SELECT total_vote FROM temp WHERE id = ?) \
                ORDER BY total_vote {rating_order}, name, id \
                LIMIT ?",
                (
                    latest_row.apt_id,
                    latest_row.apt_name,
                    latest_row.apt_id,
                    latest_row.apt_id,
                    num_apts,
                ),
            ).fetchall()
        else:
            apt_query = self.rating_sort_helper.cursor.execute(
                self.populate_query
                + f"SELECT * FROM temp \
                ORDER BY total_vote {rating_order}, name, id \
                LIMIT ?",
                (num_apts,),
            ).fetchall()
        return apt_query

    @use_database
    def price_sort_helper(
        self, num_apts: int, price_sort: int, latest_row: LatestPopulatedApt
    ) -> List[Tuple]:
        """Helper for price-only sorts"""
        price_order = "DESC" if price_sort == 1 else ""
        price_comp = "<" if price_sort == 1 else ">"
        apt_query = []
        if latest_row.apt_id >= 0:
            apt_query = self.price_sort_helper.cursor.execute(
                self.populate_query
                + f"SELECT * FROM temp \
                WHERE \
                (p_avg = (SELECT p_avg FROM temp WHERE id = ?) \
                AND (name, id) > (?, ?)) \
                OR p_avg {price_comp} (SELECT p_avg FROM temp WHERE id = ?) \
                ORDER BY p_avg {price_order}, name, id \
                LIMIT ?",
                (
                    latest_row.apt_id,
                    latest_row.apt_name,
                    latest_row.apt_id,
                    latest_row.apt_id,
                    num_apts,
                ),
            ).fetchall()
        else:
            apt_query = self.price_sort_helper.cursor.execute(
                self.populate_query
                + f"SELECT * FROM temp \
                ORDER BY p_avg {price_order}, name, id \
                LIMIT ?",
                (num_apts,),
            ).fetchall()
        return apt_query

    @use_database
    def both_sort_helper(
        self,
        num_apts: int,
        price_sort: int,
        rating_sort: int,
        latest_row: LatestPopulatedApt,
    ) -> List[Tuple]:
        """Helper to sort both params"""

        price_comp = "<" if price_sort == 1 else ">"
        price_order = "DESC" if price_sort == 1 else ""

        rating_comp = "<" if rating_sort == 1 else ">"
        rating_order = "DESC" if rating_sort == 1 else ""

        if latest_row.apt_id >= 0:
            apt_query = self.both_sort_helper.cursor.execute(
                self.populate_query
                + f"SELECT * FROM temp \
                WHERE p_avg {price_comp} (SELECT p_avg FROM temp WHERE id = ?) \
                OR ( \
                p_avg = (SELECT p_avg FROM temp WHERE id = ?) \
                AND ( \
                total_vote {rating_comp} (SELECT total_vote FROM temp WHERE id = ?) \
                OR (total_vote = (SELECT total_vote FROM temp WHERE id = ?) \
                AND (name, id) > (?, ?)) \
                ) \
                ) \
                ORDER BY p_avg {price_order}, total_vote {rating_order}, name, id \
                LIMIT ?",
                (
                    latest_row.apt_id,
                    latest_row.apt_id,
                    latest_row.apt_id,
                    latest_row.apt_id,
                    latest_row.apt_name,
                    latest_row.apt_id,
                    num_apts,
                ),
            ).fetchall()
        else:
            apt_query = self.both_sort_helper.cursor.execute(
                self.populate_query
                + f"SELECT * FROM temp \
                ORDER BY p_avg {price_order}, total_vote {rating_order}, name, id \
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
            "SELECT user_id FROM Users WHERE username = ? OR email = ?", (username, username)
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
        """Create a list of reviews out of a query"""
        reviews = []
        for entry in ratings_query:
            if entry[0] is not None:
                vote = False
                if entry[3] == 1:
                    vote = True
                reviews.append(Review(entry[0], entry[1], entry[2], vote))
        return reviews

    @use_database
    def delete_apartment_review(self, apt_id: int, username: str) -> List[Review]:
        """Delete an apartment reviews"""
        self.delete_apartment_review.cursor.execute(
            "DELETE FROM Reviews WHERE (apt_id = ? AND user_id = \
            (SELECT user_id FROM Users WHERE username = ?))",
            (apt_id, username),
        )
        self.delete_apartment_review.connection.commit()
        return self.get_apartments_reviews(apt_id)
