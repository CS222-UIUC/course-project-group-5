"""Test decorators.py"""
import sqlite3
import pytest
import decorators


@decorators.use_database
def insert_review():
    """Uses use_database for inserting a review"""
    insert_review.cursor.execute(
        "INSERT INTO Reviews (apt_id, user_id, date_of_rating, comment, vote) \
        VALUES (?, ?, ?, ?, ?)",
        (5, 5, "2022-11-06", "mock comment", 1),
    )


@decorators.use_test
def test_use_database_raise_exception():
    """use_database correctly raises an exception"""
    connection = sqlite3.connect("database/database_test.db")
    cursor = connection.cursor()
    cursor.execute(
        "INSERT INTO Reviews (apt_id, user_id, date_of_rating, comment, vote) \
        VALUES (?, ?, ?, ?, ?)",
        (5, 5, "2022-11-06", "mock comment", 1),
    )
    connection.commit()
    with pytest.raises(Exception):
        insert_review()
    cursor.execute("DELETE FROM Reviews WHERE apt_id = ?", (5,))
    connection.commit()
