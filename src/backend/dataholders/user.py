"""Contains the User class"""
from dataclasses import dataclass


@dataclass
class User:
    """Stores data for a particular User"""

    username: str
    password: str
    email: str
    phone: str
