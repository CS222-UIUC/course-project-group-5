"""Contains the UserPage backend"""
from pages.login import Login
from dataholders.user import User
from typing import List
from dataholders.apt import Apt
from decorators import use_database
from pages.login import validate_phone

class UserPage:
    """UserPage class"""

    def __init__(self, username: str) -> None:
        """Constructor"""
        self.username = username

    def get_user(self, username: str):
        """Return User object based on username"""
        return True

    def update_password(self, password: str) -> bool:
        """Updates password based on username"""
        # can use Flask-Hashing if we want 
        return True

    def update_email(self, email: str) -> bool:
        """Updates email based on username"""
        return True

    def get_liked(self, user_id: int) -> List[Apt]:
        """Gets liked apartments based on username"""
        apts = []
        return apts
    
    @use_database
    def update_phone(self, phone: str) -> bool:
        """Updates User's phone number if valid"""
        if not validate_phone(phone):
            return False
        self.update_phone.cursor.execute(
            "UPDATE Users SET phone = ? WHERE (username = ?)", (phone, self.username),
        )
        return True
