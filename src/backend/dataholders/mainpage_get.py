"""Contains dataclasses for mainpage get requests"""
from dataclasses import dataclass
from typing import Union


@dataclass
class GetRequestType:
    """Specific action of the request"""

    is_search: bool
    is_populate: bool
    is_review: bool
    is_pictures: bool


@dataclass
class Params:
    """Other request parameters"""

    num_apts: Union[int, None]
    apt_id: Union[int, None]
    search_query: Union[str, None]
    rating_sort: Union[int, None]
    price_sort: Union[int, None]
