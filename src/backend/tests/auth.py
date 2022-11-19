"""Tests password, email, and phone"""
import re


def validate_password(password: str) -> bool:
    """Used in Login and User class"""
    return len(password) >= 8


def validate_email(email: str) -> bool:
    """Used in Login and User class"""
    regex_email = re.compile(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b")
    return regex_email.fullmatch(email)


def validate_phone(phone: str) -> bool:
    """Used in Login and User class"""
    regex_phone = re.compile(
        r"^\s*(?:\+?(\d{1,3}))?[-. (]"
        r"*(\d{3})[-. )]*(\d{3})[-. ]"
        r"*(\d{4})(?: *x(\d+))?\s*$"
    )
    return regex_phone.fullmatch(phone)
