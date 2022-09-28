import pytest
from login import Login
from app import login, register, login_success, login_failure, register_success, register_failure
import sqlite3

class TestLogin:
    first_login = Login()
    username = "sadf23"
    password1 = "passw"
    password2 = "dsc"
    connection = sqlite3.connect("database.db")
    cursor = connection.cursor()
    def register_setup(self) -> bool:
        register = self.first_login.register(self.username, "akfda@gmail.com", "passwor", "213-342-123")
        return register
    def delete_register(self) -> str:
        delete = self.first_login.delete_register_for_tests(self.username)
        return delete
    def test_register(self):
        self.test_register_helper()
        # do it again to confirm
        self.test_register_helper()
    def test_register_helper(self): # I would pass in the username but it's not working
        first_register_bool = self.register_setup()
        second_register_bool = self.register_setup()
        assert first_register_bool == True
        assert second_register_bool == False
        delete = self.delete_register()
        assert delete == self.username
    def test_login(self):
        self.register_setup()
        user = self.first_login.login(1, "passw")
        check = self.cursor.execute(
            "SELECT username, email, password FROM Users WHERE (username = ? OR email = ?) \
            AND password = ?",
            (1, 1, "passw")).fetchall()
        assert user == check
        pass
        