import requests
import sqlite3


def test_register_valid():
    """Test handles valid registration"""
    reg_info = {"username": "big_finger", "email": "junk@gmail.com", "password": "pass", "phone": "0003335555"}
    res = requests.post("http://127.0.0.1:5000/register", json = reg_info)
    connection = sqlite3.connect("database/database.db")
    cursor = connection.cursor()
    cursor.execute("DELETE FROM Users WHERE username = ?", ("big_finger",))
    connection.commit()
    connection.close()
    assert res.status_code == 200 

def test_register_invalid():
    """Test handles invalid registration"""
    reg_info = {"username": "big_finger", "email": "junk@gmail.com", "password": "pass", "phone": "0003335555"}
    reg_info_2 = {"username": "big_finger", "email": "junk2@gmail.com", "password": "pass", "phone": "0003335555"}
    reg_info_3 = {"username": "fig_binger", "email": "junk&gmail.com", "password": "pass", "phone": "0003335555"}
    requests.post("http://127.0.0.1:5000/register", json = reg_info)
    res_2 = requests.post("http://127.0.0.1:5000/register", json = reg_info_2)
    res_3 = requests.post("http://127.0.0.1:5000/register", json = reg_info_3)

    connection = sqlite3.connect("database/database.db")
    cursor = connection.cursor()
    cursor.execute("DELETE FROM Users WHERE username = ?", ("big_finger",))
    connection.commit()
    connection.close()

    assert res_2.status_code == 400
    assert res_3.status_code == 400

def test_login_valid():
    """Test handles valid login"""
    connection = sqlite3.connect("database/database.db")
    cursor = connection.cursor()
    cursor.execute("INSERT INTO Users (username, password, email, phone)\
    VALUES (?, ?, ?, ?", ("big_finger", "pass", "junk@gmail.com", "0003335555"))
    connection.commit()

    log_info = {"user": "big_finger", "password": "pass"}
    res = requests.post("http://127.0.0.1:5000/login", json = log_info)
    cursor.execute("DELETE FROM Users WHERE username = ?", ("big_finger",))
    connection.commit()
    connection.close()
    assert res.status_code == 200

def test_login_invalid():
    """Test handles invalid login"""
    log_info = {"user": "big_finger", "password": "pass"}
    res = requests.post("http://127.0.0.1:5000/login", json = log_info)
    assert res.status_code == 404