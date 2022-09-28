import pytest
from login import Login
from app import login, register, login_success, login_failure, register_success, register_failure

'''
def inc(x):
    return x + 1

def test_answer():
    assert inc(3) == 4

def f():
    raise SystemExit(1)


def test_mytest():
    with pytest.raises(SystemExit):
        f()

class TestClass:
    def test_one(self):
        x = "this"
        assert "h" in x

    def test_two(self):
        x = "hello"
        assert hasattr(x, "check")
'''
class TestLogin:
    def test_register(self):
        first_login = Login()
        first_register = first_login.register("sadf23", "akfda@gmail.com", "passwor", "213-342-123")
        second_register = first_login.register("sadf23", "akfda@gmail.com", "passwor", "213-342-123")
        assert(first_register == True)
        assert(second_register == False)
        