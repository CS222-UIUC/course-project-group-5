""" Contains Login class """
from dataclasses import dataclass
import re
import sqlite3


@dataclass(frozen=True)
class RegisterResult:
    """Stores the register respond message and validity"""

    message: str
    status: bool


class Login:
    """Login class"""

    # stored_user = User()
    def __init__(self) -> None:
        """Constructor"""

    def register(
        self, username: str, email: str, password: str, phone: str
    ) -> RegisterResult:
        """Register function, returns false if username is taken"""
        if (not username) or (not email) or (not password) or (not phone):
            return RegisterResult("Missing information, please try again", False)
        regex = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"
        if not re.fullmatch(regex, email):
            return RegisterResult("Invalid email, please try again", False)
        if len(phone) != 10:
            return RegisterResult("Invalid phone number, please try again", False)
        if len(password) < 8:
            return RegisterResult("Password is too short, please try again", False)
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
            return RegisterResult(f"Register successful, welcome {username}", True)
        connection.close()
        return RegisterResult(f"{username} already registered, please try again", False)

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
        return len(user) > 0

    def logout(self) -> None:
        """Logout function"""
