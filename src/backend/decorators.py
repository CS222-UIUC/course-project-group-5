"""Stores decorators for common functionalities"""
import sqlite3
import functools


def use_database(func):
    """Decorator to utilize DB connections"""

    @functools.wraps(func)
    def wrapped(*args):
        """Wrapper about the actual function"""
        connection = sqlite3.connect("database/database.db")
        cursor = connection.cursor()
        wrapped.cursor = cursor
        wrapped.connection = connection
        try:
            caller = func(*args)
        except Exception:
            connection.rollback()
            raise
        else:
            connection.commit()
        finally:
            connection.close()
        return caller

    return wrapped
