''' Contains Login class '''
import sqlite3

class Login:
    '''Login class'''
    #stored_user = User()
    def __init__(self) -> None:
        '''Constructor'''
        self.connection = sqlite3.connect("database.db")
        self.cursor = self.connection.cursor()
    def register(self, username: str, email: str, password: str, phone: str) -> bool:
        '''Register function, returns false if username is taken'''
        if "@" not in email:
            return True
        check = self.cursor.execute("SELECT username FROM Users WHERE username = ?", (username, )).fetchall()
        if not check: # valid
            self.cursor.execute(
            "INSERT INTO Users (username, email, password, phone) VALUES (?, ?, ?, ?)",
            (username, email, password, phone))
            return True
        return False
    def delete_register_for_tests(self, username: str) -> str:
        self.cursor.execute(
        "DELETE FROM Users WHERE username = ?", (username, ))
        return username
    def login(self, username: str, password: str) -> bool:
        '''Login function, returns false if combination not found'''
        #user = self.cursor.execute(
        #    "SELECT username, email, password FROM Users WHERE (username = ? OR email = ?) \
        #    AND password = ?",
        #    (username, email, password)).fetchall()
        user = self.cursor.execute(
            "SELECT username, password FROM Users WHERE username = ? \
            AND password = ?",
            (username, password)).fetchall()
        return user
    def logout(self) -> None:
        '''Logout function'''
