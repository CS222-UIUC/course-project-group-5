"""Test login.py"""
import sqlite3
from login import Login

# from app import login, register, login_success, login_failure, register_success, register_failure
class TestLogin:
    """Test Login class"""

    first_login = Login()
    username = "sadf23"
    password1 = "passw"
    connection = sqlite3.connect("database/database.db")
    cursor = connection.cursor()

    def register_setup(self) -> bool:
        """Registers a user with first_login object"""
        register = self.first_login.register(
            self.username, "akfda@gmail.com", "passwor", "213-342-123"
        )
        return register

    def delete_register(self) -> str:
        """Remove fake data from database"""
        self.first_login.cursor.execute(
            "DELETE FROM Users WHERE username = ?", (self.username,)
        )
        return self.username

    def test_register(self):
        """Tests register function"""
        self.test_register_helper()
        # do it again to confirm
        self.test_register_helper()

    def test_register_helper(self):
        """Registers users and tests duplicate usernames"""
        first_register_bool = self.register_setup()
        second_register_bool = self.register_setup()
        assert first_register_bool is True
        assert second_register_bool is False
        delete = self.delete_register()
        assert delete == self.username  # correct data deleted

    def test_login(self):
        """Tests login function"""
        self.register_setup()
        user = self.first_login.login(self.username, "passw")
        check = self.cursor.execute(
            "SELECT username, email, password FROM Users WHERE (username = ? OR email = ?) \
            AND password = ?",
            (self.username, "email", "passw"),
        ).fetchall()
        assert user == check

    def test_logout(self):
        """Tests logout function"""
