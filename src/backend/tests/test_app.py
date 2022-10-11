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
    """Test register handles valid registration"""
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


def test_register_duplicate_username(client):
    """Test register handles duplicate username"""
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


def test_register_missing_field(client):
    """Test register handles missing field"""
    reg_info = {
        "username": "big_finger",
        "email": "",
        "password": "123456789",
        "phone": "0003335555",
    }
    res = client.post("/register", json=reg_info)
    connection = sqlite3.connect("database/database.db")
    cursor = connection.cursor()
    cursor.execute("DELETE FROM Users WHERE username = ?", ("big_finger",))
    connection.commit()
    connection.close()
    assert res.status_code == 400


def test_register_invalid_email_format(client):
    """Test register handles invalid email format"""
    reg_info = {
        "username": "fig_binger",
        "email": "junk&gmail.com",
        "password": "123456789",
        "phone": "0003335555",
    }
    res = client.post("/register", json=reg_info)
    assert res.status_code == 400


def test_register_invalid_phone_number_length(client):
    """Test registers handle invalid phone number length"""
    reg_info = {
        "username": "fig_binger",
        "email": "junk@gmail.com",
        "password": "123456789",
        "phone": "000333",
    }
    res = client.post("/register", json=reg_info)
    assert res.status_code == 400


def test_register_short_password(client):
    """Test register handles short password"""
    reg_info = {
        "username": "fig_binger",
        "email": "junk@gmail.com",
        "password": "123456",
        "phone": "0003335555",
    }
    res = client.post("/register", json=reg_info)
    assert res.status_code == 400


def test_login_valid(client):
    """Test handles valid login"""
    connection = sqlite3.connect("database/database.db")
    cursor = connection.cursor()
    cursor.execute(
        "INSERT INTO Users (username, password, email, phone)\
    VALUES (?, ?, ?, ?)",
        ("big_finger", "pass", "junk@gmail.com", "0003335555"),
    )
    connection.commit()

    log_info = {"user": "big_finger", "password": "pass"}
    res = client.post("/login", json=log_info)
    cursor.execute("DELETE FROM Users WHERE username = ?", ("big_finger",))
    connection.commit()
    connection.close()
    assert res.status_code == 200


def test_login_invalid(client):
    """Test handles invalid login"""
    log_info = {"user": "big_finger", "password": "pass"}
    res = client.post("/login", json=log_info)
    assert res.status_code == 404
