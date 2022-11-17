"""Contains the UserPage backend"""
from typing import List
from pages.login import validate_phone
from dataholders.user import User
from dataholders.apt import Apt
from decorators import use_database


class UserPage:
    """UserPage class"""

    def __init__(self, username: str) -> None:
        """Constructor"""
        self.username = username
        self.user = self.get_user(username)

    @use_database
    def get_user(self, username: str):
        """Return User object based on username"""
        query_sql = "%" + username + "%"
        user_query = self.get_user.cursor.execute(
            "SELECT u.user_id, u.password, u.email, u.phone \
            FROM USERS u\
            WHERE u.username = ?",
            (query_sql,),
        ).fetchone()
        if user_query is None:
            return None
        user_id, password, email, phone = user_query
        return User(user_id, username, password, email, phone)

    @use_database
    def update_password(self, password: str) -> bool:
        """Updates password based on username"""
        # can use Flask-Hashing if we want
        if self.user.password == password:
            return True
        query_sql = "%" + self.user.user_id + "%"
        self.update_password.cursor.execute(
            "UPDATE Users \
            SET password = ? \
            WHERE user_id = ?",
            (password, query_sql),
        )
        return True

    @use_database
    def update_email(self, email: str) -> bool:
        """Updates email based on username"""
        if self.user.email == email:
            return True

        query_sql = "%" + email + "%"
        self.update_email.cursor.execute(
            "UPDATE Users \
            SET email = ? \
            WHERE username = ?",
            (query_sql, self.username),
        )
        new_email = self.update_email.cursor.execute(
            "SELECT email \
            From User \
            WHERE username = ?",
            (self.username),
        ).fetchone()[0]

        return new_email == email

    @use_database
    def get_liked(self, user_id: int) -> List[Apt]:
        """Gets liked apartments based on username"""
        apts = []
        query_sql = "%" + user_id + "%"
        liked = self.get_liked.cursor.execute(
            "SELECT a.apt_id, a.apt_name, a.apt_address, a.price_min, a.price_max \
            From Reviews r INNER JOIN Apartments a \
            ON r.apt_id = a.apt_id \
            WHERE r.user_id = ? AND r.vote = ?",
            (query_sql, 1),
        )

        for apt in liked:
            apt_id, apt_name, apt_address, price_min, price_max = apt
            query_sql = "%" + apt_id + "%"
            rating = self.get_liked.cursor.execute(
                "SELECT AVG(r.vote) \
                From Reviews r \
                WHERE r.apt_id = ?",
                (query_sql),
            )
            apts.append(
                Apt(apt_id, apt_name, rating, apt_address, price_min, price_max)
            )
        return apts

    @use_database
    def update_phone(self, phone: str) -> bool:
        """Updates User's phone number if valid"""
        if not validate_phone(phone):
            return False
        self.update_phone.cursor.execute(
            "UPDATE Users SET phone = ? WHERE (username = ?)",
            (phone, self.username),
        )
        self.update_phone.connection.commit()
        return True