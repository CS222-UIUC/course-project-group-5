import sqlite3

class Login:
    #stored_user = User()
    def __init__(self) -> None:
        self.connection = sqlite3.connect("database.db")
        self.cursor = self.connection.cursor()
    def register(self, username: str, email: str, password: str, phone: str) -> bool:
        check = self.cursor.execute("SELECT username FROM Users WHERE username = ?", username)
        if not check:
            self.cursor.execute("INSERT INTO Users (username, email, password, phone) VALUES (?, ?, ?, ?)", username, email, password, phone)
            return True
        else:
            return False
    def login(self, user_id: str, password: str) -> bool:
        user = self.cursor.execute("SELECT username, email, password FROM Users WHERE (username = ? OR email = ?) AND password = ?", user_id, password)
        return user
    def logout(self) -> None:
        pass