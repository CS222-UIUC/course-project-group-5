"""Stores decorators for common functionalities"""
import sqlite3
from functools import wraps
import config
from app import session

def use_database(func):
    """Decorator to utilize DB connections"""

    @wraps(func)
    def wrapped(*args):
        """Wrapper around the actual function"""
        connection = sqlite3.connect(f"database/{config.DB_NAME}")
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


def use_test(func):
    """Decorator to switch database for testing"""

    @wraps(func)
    def wrapped(*args, **kwargs):
        """Wrapper around the actual function"""
        config.DB_NAME = "database_test.db"
        func_instance = func(*args, **kwargs)
        config.DB_NAME = "database_prod.db"
        return func_instance

    return wrapped
'''
def login_required(func):
    """Decorator to prevent logged out user entering user page"""

    @wraps(func)
    def wrapped(*args, **kwargs):
        """Wrapper"""
        if session.get("USERNAME", None) is None:
            return {"url": "/register"}, 404
        return func(*args, **kwargs)

    return wrapped
    '''