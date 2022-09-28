import pytest
from login import Login
from app import login, register, login_success, login_failure, register_success, register_failure
import sqlite3

class TestLogin:
    first_login = Login()
    username = "sadf23"
    def test_register(self):
        self.test_register_helper()
        # do it again to confirm
        self.test_register_helper()
    def test_register_helper(self): # I would pass in the username but it's not working
        first_register_bool = self.first_login.register(self.username, "akfda@gmail.com", "passwor", "213-342-123")
        second_register_bool = self.first_login.register(self.username, "akfda@gmail.com", "passwor", "213-342-123")
        assert first_register_bool == False
        assert second_register_bool == True
        delete = self.first_login.delete_register_for_tests(self.username)
        assert delete == self.username
    def test_login(self):
        pass
        