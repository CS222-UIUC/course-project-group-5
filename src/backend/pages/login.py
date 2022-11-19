""" Contains Login class """
from dataclasses import dataclass
from decorators import use_database
from tests.auth import validate_email, validate_password, validate_phone


@dataclass(frozen=True)
class RegisterResult:
    """Stores the register respond message and validity"""

    message: str
    status: bool


class Login:
    """Login class"""

    def __init__(self) -> None:
        """Constructor"""

    @use_database
    def register(
        self, username: str, email: str, password: str, phone: str
    ) -> RegisterResult:
        """Register function, returns false if username is taken"""
        if (not username) or (not email) or (not password) or (not phone):
            return RegisterResult("Missing information, please try again", False)

        if not validate_email(email):
            return RegisterResult("Invalid email, please try again", False)

        if not validate_phone(phone):
            return RegisterResult("Invalid phone number, please try again", False)

        if not validate_password(password):
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
        """Logout"""
