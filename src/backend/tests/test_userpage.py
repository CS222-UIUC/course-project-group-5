"""Test userpage.py"""
import sqlite3
from pages.userpage import UserPage
#from decorators import use_test, use_database
#from pages.login import validate_phone
from app import app

class TestUserPage:
    """Test user page class"""

    userpage = UserPage()
    phone = "012-345-6789"
    invalid_phone = "123-3421-322"
    
    #@use_database
    def set_up(self):
        with app.test_client() as c:
            with c.session_transaction() as session:
                session["SECRET_KEY"] = "VlpJb4lFReaMsVvPZgzMJA"
            result = app.test_client.get('/')

    #@use_database
    def test_update_phone(self):
        """Tests valid and invalid phone numbers"""
        #assert validate_phone(self.phone) is True # verify for later tests
        #assert validate_phone(self.invalid_phone) is False
        #valid = self.test_valid_phone(self.phone)
        #invalid = self.test_invalid_phone(self.invalid_phone)
        #assert valid is True
        #assert invalid is False

    #@use_database
    def test_valid_phone(self) -> bool:
        """Test update_phone returns True and User is logged in"""
        connection = sqlite3.connect("database/database_test.db")
        cursor = connection.cursor()
        cursor.execute(
                "INSERT INTO Users (username, email, password, phone, apt_id) \
                VALUES (?, ?, ?, ?, 0)",
                ("hello", "hello@gmail.com", "password", "011-899-9013"),
        )
        cursor.execute(
                "UPDATE Users SET phone = ? WHERE (username = ?)", (self.phone, "hello"),
        )
        result = cursor.execute("SELECT phone FROM Users WHERE (username = ?)", ("hello",)).fetchone()
        #update = self.userpage.update_phone(self.valid)
        return True

    def test_invalid_phone(self) -> bool:
        """Test update_phone returns False"""
        update = self.userpage.update_phone(self.invalid_phone)
        return True

    def cleanup_db(self) -> None:
        """Remove fake data from database"""
        connection = sqlite3.connect("database/database_test.db")
        cursor = connection.cursor
        cursor.execute("DELETE FROM Users WHERE (phone = ?)", (self.phone,))
        cursor.execute("DELETE FROM Users WHERE (phone = ?)", (self.invalid_phone,))
        connection.commit()
        connection.close()
