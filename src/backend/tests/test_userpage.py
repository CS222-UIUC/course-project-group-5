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
    def test_update_phone(self):
        """Tests valid and invalid phone numbers"""
        assert validate_phone(self.phone) is True # verify for later tests
        assert validate_phone(self.invalid_phone) is False
        valid = self.test_valid_phone()
        invalid = self.test_invalid_phone()
        assert valid is True
        assert invalid is False
        self.cleanup_db()

    @use_test
    def test_valid_phone(self) -> bool:
        """Test update_phone returns True and User is logged in"""
        connection = sqlite3.connect("database/database_test.db")
        cursor = connection.cursor()
        cursor.execute(
                "INSERT INTO Users (username, email, password, phone, apt_id) \
                VALUES (?, ?, ?, ?, 0)",
                (self.alt_username, "hello@gmail.com", "password", "011-899-9013"),
        )
        cursor.execute(
                "UPDATE Users SET phone = ? WHERE (username = ?)", (self.phone, self.alt_username,),
        )
        result = cursor.execute("SELECT phone FROM Users WHERE (username = ?)", (self.alt_username,)).fetchone()
        update = self.userpage.update_phone(self.phone)
        assert result == update
        self.cleanup_db()
        return update
    
    @use_test
    def test_invalid_phone(self) -> bool:
        """Test update_phone returns False"""
        return self.userpage.update_phone(self.invalid_phone)

    @use_test
    def cleanup_db(self) -> None:
        """Remove fake data from database"""
        connection = sqlite3.connect("database/database_test.db")
        cursor = connection.cursor()
        cursor.execute("DELETE FROM Users WHERE (username = ?)", (self.username, self.alt_username,))
        connection.commit()
        connection.close()
