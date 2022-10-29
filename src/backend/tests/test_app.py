"""Test app.py"""
import sqlite3
import pytest
from app import app
from tests.mainpage_staging import MainPageStaging


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


def test_mainpage_get_valid(client):
    """Test mainpage handles valid get request"""
    mainpage = MainPageStaging()
    mainpage.initialize_all()
    connection = sqlite3.connect("database/database.db")
    cursor = connection.cursor()

    far_id = cursor.execute(
        "SELECT apt_id FROM Apartments WHERE (apt_name = 'FAR')"
    ).fetchone()[0]

    res = client.get("/main", query_string={"review": "True", "aptId": far_id})
    sample_json = (
        '[{"username": "Big_finger", '
        '"date": "2022-10-10", '
        '"comment": "Decent hall", '
        '"vote": true}]'
    )

    connection.close()
    mainpage.clean_all()
    assert res.status_code == 200
    assert res.text == sample_json


def test_mainpage_get_invalid(client):
    """Test mainpage handles invalid get request"""
    res = client.get("/main", query_string={"search": "True"})
    assert res.status_code == 400


def test_mainpage_post_valid(client):
    """Test mainpage handles valid post request"""
    mainpage = MainPageStaging()
    mainpage.initialize_all()
    connection = sqlite3.connect("database/database.db")
    cursor = connection.cursor()

    isr_id = cursor.execute(
        "SELECT apt_id FROM Apartments WHERE (apt_name = 'ISR')"
    ).fetchone()[0]
    sample_review = {
        "apt_id": isr_id,
        "username": "Minh Phan",
        "comment": "Good",
        "vote": 1,
    }
    res = client.post("/main", json=sample_review)

    cursor.execute("DELETE FROM Reviews WHERE apt_id = ?", (isr_id,))
    connection.commit()
    connection.close()
    mainpage.clean_all()
    assert res.status_code == 201


def test_mainpage_post_invalid(client):
    """Test mainpage handles invalid post request"""
    sample_review = {"username": "User McUserFace", "comment": "Ho ho ho ho"}
    res = client.post("/main", json=sample_review)
    assert res.status_code == 400
