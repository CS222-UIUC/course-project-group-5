""" Contains Login class """
import sqlite3


class Login:
    """Login class"""

    # stored_user = User()
    def __init__(self) -> None:
        """Constructor"""

    def register(self, username: str, email: str, password: str, phone: str) -> bool:
        """Register function, returns false if username is taken"""
        if "@" not in email:
            return False
        connection = sqlite3.connect("database/database.db")
        cursor = connection.cursor()
        check = cursor.execute(
            "SELECT username FROM Users WHERE username = ?", (username,)
        ).fetchone()
        if check is None:  # valid
            cursor.execute(
                "INSERT INTO Users (username, email, password, phone, apt_id) \
                VALUES (?, ?, ?, ?, 0)",
                (username, email, password, phone),
            )
            connection.commit()
            connection.close()
            return True
        connection.close()
        return False

    def login(self, user_id: str, password: str) -> bool:
        """Login function, returns false if combination not found"""
        connection = sqlite3.connect("database/database.db")
        cursor = connection.cursor()
        user = cursor.execute(
            "SELECT username, email, password FROM Users WHERE (username = ? OR email = ?) \
            AND password = ?",
            (user_id, user_id, password),
        ).fetchall()
        connection.close()
        return user

    def logout(self) -> None:
        """Logout function"""
