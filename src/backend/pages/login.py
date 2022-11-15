""" Contains Login class """
from dataclasses import dataclass
import re
from decorators import use_database
#from app import session


@dataclass(frozen=True)
class RegisterResult:
    """Stores the register respond message and validity"""

    message: str
    status: bool


class Login:
    """Login class"""

    # stored_user = User()
    def __init__(self) -> None:
        """Constructor"""

    @use_database
    def register(
        self, username: str, email: str, password: str, phone: str
    ) -> RegisterResult:
        """Register function, returns false if username is taken"""
        if (not username) or (not email) or (not password) or (not phone):
            return RegisterResult("Missing information, please try again", False)

        regex_email = re.compile(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b")
        if not regex_email.fullmatch(email):
            return RegisterResult("Invalid email, please try again", False)

        if not self.validate_phone(phone):
            return RegisterResult("Invalid phone number, please try again", False)

        if len(password) < 8:
            return RegisterResult("Password is too short, please try again", False)

        check = self.register.cursor.execute(
            "SELECT username FROM Users WHERE username = ?", (username,)
        ).fetchone()
        if check is None:  # valid
            self.register.cursor.execute(
                "INSERT INTO Users (username, email, password, phone, apt_id) \
                VALUES (?, ?, ?, ?, 0)",
                (username, email, password, phone),
            )
            return RegisterResult(f"Register successful, welcome {username}", True)
        return RegisterResult(f"{username} already registered, please try again", False)

    @use_database
    def login(self, user_id: str, password: str) -> bool:
        """Login function, returns false if combination not found"""
        user = self.login.cursor.execute(
            "SELECT username, email, password FROM Users WHERE (username = ? OR email = ?) \
            AND password = ?",
            (user_id, user_id, password),
        ).fetchall()
        return len(user) > 0

    def logout(self) -> None:
        """Logout function removes session object"""
        #session.pop("USERNAME", None) # session object is None if pop fails

def validate_phone(phone: str) -> bool:
    """Used in Login class and in User class"""
    regex_phone = re.compile(
        r"^\s*(?:\+?(\d{1,3}))?[-. (]"
        r"*(\d{3})[-. )]*(\d{3})[-. ]"
        r"*(\d{4})(?: *x(\d+))?\s*$"
    )
    if not regex_phone.fullmatch(phone):
        return False
    return True
