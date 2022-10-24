"""Contains Apartment class"""
from dataclasses import dataclass
from marshmallow import Schema, fields

@dataclass
class Apt:
    """Apt class, stores detail about an apartment"""

    apt_id: int
    name: str
    address: str
    rating: int
    price_min: int
    price_max: int

class ObjectSchema(Schema):
    apt_id = fields.Int()
    name = fields.Str()
    address = fields.Str()
    review = fields.Str()
    image = fields.Str()
    rating = fields.Int()
    price_min = fields.Int()
    price_max = fields.Int()