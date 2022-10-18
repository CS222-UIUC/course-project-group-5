"""Test login.py"""
import sqlite3
from login import Login

class TestLogin:
    """Test Login class"""

    first_login = Login()
    username = "sadf23"
    password1 = "passw"

    def register_setup(self) -> bool:
        """Registers a user with first_login object"""
        register = self.first_login.register(
            self.username, "akfda@gmail.com", "123456789", "213-342-1234"
        )
        return register.status

    def delete_register(self) -> str:
        """Remove fake data from database"""
        connection = sqlite3.connect("database/database.db")
        cursor = connection.cursor()
        cursor.execute("DELETE FROM Users WHERE username = ?", (self.username,))
        connection.commit()
        connection.close()
        return self.username

    def test_register(self):
        """Tests register function"""
        self.register_helper()
        # do it again to confirm
        self.register_helper()

    def register_helper(self):
        """Registers users and tests duplicate usernames"""
        first_register_bool = self.register_setup()
        second_register_bool = self.register_setup()
        assert first_register_bool is True
        assert second_register_bool is False
        delete = self.delete_register()
        assert delete == self.username  # correct data deleted

    def test_register_invalid_email(self):
        """Invalid email string"""
        register = self.first_login.register(
            self.username, "akfda&gmail.com", "123456789", "213-342-1234"
        )
        register_2 = self.first_login.register(
            self.username, "akfda@gmail", "123456789", "213-342-1234"
        )
        assert register.status is False
        assert register_2.status is False

    def test_register_missing_field(self):
        """Missing certain fields"""
        register = self.first_login.register(
            self.username, "", "123456789", "213-342-1234"
        )
        assert register.status is False

    def test_register_short_password(self):
        """Password is too short"""
        register = self.first_login.register(
            self.username, "akfda@gmail.com", "1234567", "213-342-1234"
        )
        assert register.status is False

    def test_register_invalid_phone_length(self):
        """Invalid phone number length"""
        register = self.first_login.register(
            self.username, "akfda@gmail.com", "123456789", "213-342-123"
        )
        assert register.status is False

    def test_login(self):
        """Tests login function"""
        self.register_setup()
        user = self.first_login.login(self.username, "123456789")
        self.delete_register()
        assert user is True

    def test_login_invalid(self):
        """Test invalid login attempt"""
        user = self.first_login.login(self.username, "123456789")
        assert user is False

    def test_logout(self):
        """Tests logout function"""
