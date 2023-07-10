"""Contains Apartment class"""
from dataclasses import dataclass


@dataclass
class Apt:
    """Apt class, stores detail about an apartment"""

    apt_id: int
    name: str
    address: str
    rating: int
    price_min: int
    price_max: int
