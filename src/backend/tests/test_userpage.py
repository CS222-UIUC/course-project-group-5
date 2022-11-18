"""Test userpage.py"""
import sqlite3
from decorators import use_test, use_database
from tests.mainpage_staging import MainPageStaging
from pages.userpage import UserPage
from dataholders.apt import Apt


class TestUserPage:
    """Test user page class"""

    username = "test_username"
    phone = "012-345-6789"
    password = "newpassword1234"
    email = "newemail@gmail.com"
    userpage = None
    main_page_staging = MainPageStaging()

    @use_database
    def initialize(self):
        """Set up tests by inserting a user into the db"""
        connection = self.initialize.connection
        cursor = self.initialize.cursor
        self.insert_users(cursor, connection)
        self.userpage = UserPage(self.username)

    def insert_users(self, cursor: sqlite3.Cursor, connection: sqlite3.Connection):
        """Initialize users for testing"""
        cursor.execute(
            "INSERT INTO Users (username, password, email, phone) \
            VALUES (?, ?, ?, ?)",
            (
                self.username,
                "beginpassword",
                "beginemail@gmail.com",
                "111-555-0022",
            ),
        )
        connection.commit()

    @use_test
    def test_invalid_input(self):
        """invalid input returns False"""
        self.initialize()
        assert self.userpage.update_password("inv2341") is False
        assert self.userpage.update_email("testemail@") is False
        assert self.userpage.update_phone("123-3421-322") is False

    @use_test
    def test_get_user(self):
        """get_user returns correct Use"""
        self.initialize()
        res = self.userpage.get_user(self.username)
        assert res.username == self.username
        assert res.password == "beginpassword"
        assert res.email == "beginemail@gmail.com"
        assert res.phone == "111-555-0022"
        assert self.userpage.get_user("sd") is None

    @use_test
    def test_valid_password(self):
        """update_password returns True and db entry is correct"""
        self.initialize()
        res = self.userpage.update_password(self.password)
        assert res is True
        connection = sqlite3.connect("database/database_test.db")
        cursor = connection.cursor()
        test_result = cursor.execute(
            "SELECT password FROM Users WHERE (username = ?)", (self.username,)
        ).fetchone()[0]
        connection.close()
        same_password = self.userpage.update_password(self.password)
        assert same_password is True
        self.cleanup_db()
        assert test_result == self.password

    @use_test
    def test_valid_email(self):
        """update_email returns True and db entry is correct"""
        self.initialize()
        res = self.userpage.update_email(self.email)
        assert res is True
        connection = sqlite3.connect("database/database_test.db")
        cursor = connection.cursor()
        test_result = cursor.execute(
            "SELECT email FROM Users WHERE (username = ?)", (self.username,)
        ).fetchone()[0]
        connection.close()
        same_email = self.userpage.update_email(self.email)
        assert same_email is True
        self.cleanup_db()
        assert test_result == self.email

    @use_test
    def test_valid_phone(self):
        """update_phone returns True and db entry is correct"""
        self.initialize()
        res = self.userpage.update_phone(self.phone)
        assert res is True
        connection = sqlite3.connect("database/database_test.db")
        cursor = connection.cursor()
        test_result = cursor.execute(
            "SELECT phone FROM Users WHERE (username = ?)", (self.username,)
        ).fetchone()[0]
        connection.close()
        same_phone = self.userpage.update_phone(self.phone)
        assert same_phone is True
        self.cleanup_db()
        assert test_result == self.phone

    @use_test
    def cleanup_db(self):
        """Remove fake data from database"""
        connection = sqlite3.connect("database/database_test.db")
        cursor = connection.cursor()
        cursor.execute("DELETE FROM Users WHERE (username = ?)", (self.username,))
        connection.commit()
        connection.close()

    @use_test
    def test_get_liked(self):
        """returns correct List"""
        self.initialize()
        self.main_page_staging.initialize_all()
        connection = sqlite3.connect("database/database_test.db")
        cursor = connection.cursor()
        minh_phan_id = cursor.execute(
            "SELECT user_id FROM Users WHERE (username = 'Minh Phan')"
        ).fetchone()[0]
        sherman_id = cursor.execute(
            "SELECT apt_id FROM Apartments WHERE (apt_name = 'Sherman')"
        ).fetchone()[0]
        res = self.userpage.get_liked(minh_phan_id)
        liked = []
        liked.append(Apt(sherman_id, "Sherman", "909 S 5th St", 0.333, 5500, 6500))
        self.main_page_staging.clean_all()
        assert res == liked
