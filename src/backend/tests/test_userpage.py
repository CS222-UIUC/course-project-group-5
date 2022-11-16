"""Test userpage.py"""
import sqlite3
from pages.userpage import UserPage
from decorators import use_test
from pages.login import validate_phone


class TestUserPage:
    """Test user page class"""

    username = "test_username"
    alt_username = "alt_username"
    userpage = UserPage(username)
    phone = "012-345-6789"
    invalid_phone = "123-3421-322"

    @use_test
    def test_valid_phone(self) -> bool:
        """Test update_phone returns True and db entry is the same"""
        assert validate_phone(self.phone) is True
        assert self.userpage.update_phone(self.phone) is True

        # mimics update_phone
        connection = sqlite3.connect("database/database_test.db")
        cursor = connection.cursor()
        cursor.execute(
            "INSERT INTO Users (username, email, password, phone) \
                VALUES (?, ?, ?, ?)",
            (self.alt_username, "hello@gmail.com", "password", "011-899-9013"),
        )
        connection.commit()
        cursor.execute(
            "UPDATE Users SET phone = ? WHERE (username = ?)",
            (
                self.phone,
                self.alt_username,
            ),
        )
        connection.commit()
        test_result = cursor.execute(
            "SELECT phone FROM Users WHERE (username = ?)", (self.alt_username,)
        ).fetchone()[0]
        self.cleanup_db()
        assert test_result == self.phone

    @use_test
    def test_invalid_phone(self) -> bool:
        """Test update_phone returns False"""
        assert validate_phone(self.invalid_phone) is False
        assert self.userpage.update_phone(self.invalid_phone) is False

    @use_test
    def cleanup_db(self) -> None:
        """Remove fake data from database"""
        connection = sqlite3.connect("database/database_test.db")
        cursor = connection.cursor()
        cursor.execute("DELETE FROM Users WHERE (username = ?)", (self.username,))
        cursor.execute("DELETE FROM Users WHERE (username = ?)", (self.alt_username,))
        connection.commit()
        connection.close()
