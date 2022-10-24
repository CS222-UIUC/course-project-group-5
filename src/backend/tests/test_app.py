"""Test app.py"""
import sqlite3
import pytest
from app import app


@pytest.fixture(name="config_app")
def fixture_config_app():
    """Configure the Flask object"""
    app.config.update({"TESTING": True})
    yield app


@pytest.fixture(name="client")
def fixture_client(config_app):
    """Return a test client"""
    return config_app.test_client()


def test_register_valid(client):
    """Test register returns valid (200) network code"""
    reg_info = {
        "username": "big_finger",
        "email": "junk@gmail.com",
        "password": "123456789",
        "phone": "0003335555",
    }
    res = client.post("/register", json=reg_info)
    connection = sqlite3.connect("database/database.db")
    cursor = connection.cursor()
    cursor.execute("DELETE FROM Users WHERE username = ?", ("big_finger",))
    connection.commit()
    connection.close()
    assert res.status_code == 200


def test_register_invalid(client):
    """Test register returns invalid (400) network code"""
    reg_info = {
        "username": "big_finger",
        "email": "junk@gmail.com",
        "password": "123456789",
        "phone": "0003335555",
    }
    reg_info_2 = {
        "username": "big_finger",
        "email": "junk2@gmail.com",
        "password": "123456789",
        "phone": "0003335555",
    }

    client.post("/register", json=reg_info)
    res_2 = client.post("/register", json=reg_info_2)

    connection = sqlite3.connect("database/database.db")
    cursor = connection.cursor()
    cursor.execute("DELETE FROM Users WHERE username = ?", ("big_finger",))
    connection.commit()
    connection.close()

    assert res_2.status_code == 400


def test_login_valid(client):
    """Test login returns valid (200) network code"""
    connection = sqlite3.connect("database/database.db")
    cursor = connection.cursor()
    cursor.execute(
        "INSERT INTO Users (username, password, email, phone)\
    VALUES (?, ?, ?, ?)",
        ("big_finger", "123456789", "junk@gmail.com", "0003335555"),
    )
    connection.commit()

    log_info = {"user": "big_finger", "password": "123456789"}
    res = client.post("/login", json=log_info)
    cursor.execute("DELETE FROM Users WHERE username = ?", ("big_finger",))
    connection.commit()
    connection.close()
    assert res.status_code == 200


def test_login_invalid(client):
    """Test login returns invalid (404) network code"""
    log_info = {"user": "big_finger", "password": "123456789"}
    res = client.post("/login", json=log_info)
    assert res.status_code == 404


def test_query_invalid(client):
    """A query is invalid when a query is empty"""
    query_info = {"q": "", "selected": []}
    res = client.post("/home", json=query_info)
    assert res.status_code == 400


def test_query_none_selected(client):
    """Test query"""
    connection = sqlite3.connect("database/database.db")
    cursor = connection.cursor()
    cursor.execute(
        "INSERT INTO Apartments (apt_name, apt_address, price_min, price_max, link) \
            VALUES (?, ?, ?, ?, ?)",
        ("smile", "909 S 5th St", 5500, 6500, ""),
    )
    connection.commit()
    query_info = {"q": "smile", "selected": []}
    res = client.post("/home", json=query_info)
    cursor.execute("DELETE FROM Apartments WHERE apt_name = ?", ("smile",))
    connection.commit()
    connection.close()
    assert res.status_code == 200
