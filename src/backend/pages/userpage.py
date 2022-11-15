"""Contains the UserPage backend"""
#from pages.login import Login
from dataholders.user import User
from typing import List
from dataholders.apt import Apt
#from app import session
#from decorators import use_database
from pages.login import validate_phone

class UserPage:
    """UserPage class"""

    def __init__(self) -> None:
        """Constructor"""

    def get_user(self, username: str) -> User:
        user = []
        return user

    def update_password(self, password: str) -> bool:
        # can use Flask-Hashing if we want 
        return True

    def update_email(self, email: str) -> bool:
        return True

    def get_liked(self, user_id: int) -> List[Apt]:
        apts = []
        return apts
    
    #@use_database
    def update_phone(self, phone: str) -> bool:
        """Update phone number, return true if phone is valid and database is updated"""
        '''if not validate_phone(phone):
            return False'''
        '''if session.get("USERNAME", None) is not None: # checks session object exists
            username = session.get("USERNAME") # gets the username from the session object
            self.update_phone.cursor.execute(
                "UPDATE Users SET phone = ? WHERE (username = ?)", (phone, username),
            )
            return True'''
        return False
