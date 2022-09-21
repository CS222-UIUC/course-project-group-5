import sqlite3

class Login:
    #stored_user = User()
    def __init__(self) -> None:
        self.connection = sqlite3.connect("database.db")
        self.cursor = self.connection.cursor()
    def register(self, username: str, email: str, password: str, phone: str) -> None:
        self.cursor.execute("INSERT INTO Users (username, email, password, phone) VALUES (?, ?, ?, ?)", username, email, password, phone)
        #stored_user.load_user_register(username, email, password)
    def login(self, user_id: str, password: str) -> bool:
        user = self.cursor.execute("SELECT username, email, password FROM Users WHERE (username = ? OR email = ?) AND password = ?", user_id, password)
        #stored_user.load_user(username, email, password)
        return user
    def logout(self) -> None:
        pass
    #def is_authenticated(self) -> bool:
    #    return stored_user.is_valid()
    #def get_id(self) -> str:
    #    return stored_user.id()
    #def get_name(self) -> str:
    #    return stored_user.name()