"""Contains Review class"""
from dataclasses import dataclass


@dataclass
class Review:
    """Rating class, stores details about a particular user review"""

    username: str
    date: str
    comment: str
    vote: bool
