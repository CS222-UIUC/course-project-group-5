"""Test mainpage.py invalid calls"""
import sqlite3
from mainpage import MainPage


class TestMainPageInvalid:
    """Test invalid calls to MainPage methods"""

    main_page = MainPage()

    def insert_apartments(self, cursor: sqlite3.Cursor, connection: sqlite3.Connection):
        """Insert apartments for use by test methods"""
        args = [
            ("Sherman", "909 S 5th St", 5500, 6500, ""),
            ("FAR", "901 W College Ct", 6000, 7000, ""),
            ("Lincoln", "1005 S Lincoln Ave", 5000, 6000, ""),
            ("PAR", "901 W College Ct", 5000, 6000, ""),
        ]
        cursor.executemany(
            "INSERT INTO Apartments (apt_name, apt_address, price_min, price_max, link) \
            VALUES (?, ?, ?, ?, ?)",
            args,
        )
        connection.commit()

    def insert_users(self, cursor: sqlite3.Cursor, connection: sqlite3.Connection):
        """Initialize users for use by test methods"""
        args = [
            ("Minh Phan", "", "", ""),
            ("Minh", "", "", ""),
            ("Big_finger", "", "", ""),
        ]
        cursor.executemany(
            "INSERT INTO Users (username, password, email, phone) \
            VALUES (?, ?, ?, ?)",
            args,
        )
        connection.commit()

    def insert_pics(self, cursor: sqlite3.Cursor, connection: sqlite3.Connection):
        """Initialize pics for use by test methods"""
        sherman_id = cursor.execute(
            "SELECT apt_id FROM Apartments WHERE (apt_name = 'Sherman')"
        ).fetchone()[0]
        args = [
            (sherman_id, "Link1"),
            (sherman_id, "Link2"),
            (sherman_id, "Link3"),
        ]
        cursor.executemany("INSERT INTO AptPics (apt_id, link) VALUES (?, ?)", args)
        connection.commit()

    def insert_reviews(self, cursor: sqlite3.Cursor, connection: sqlite3.Connection):
        """Initialize reviews for use by test methods"""
        sherman_id = cursor.execute(
            "SELECT apt_id FROM Apartments WHERE (apt_name = 'Sherman')"
        ).fetchone()[0]
        far_id = cursor.execute(
            "SELECT apt_id FROM Apartments WHERE (apt_name = 'FAR')"
        ).fetchone()[0]
        par_id = cursor.execute(
            "SELECT apt_id FROM Apartments WHERE (apt_name = 'PAR')"
        ).fetchone()[0]
        minh_phan_id = cursor.execute(
            "SELECT user_id FROM Users WHERE (username = 'Minh Phan')"
        ).fetchone()[0]
        minh_id = cursor.execute(
            "SELECT user_id FROM Users WHERE (username = 'Minh')"
        ).fetchone()[0]
        big_finger_id = cursor.execute(
            "SELECT user_id FROM Users WHERE (username = 'Big_finger')"
        ).fetchone()[0]
        cursor.execute(
            "INSERT INTO Ratings (apt_id, user_id, date_of_rating, comment, vote) \
            VALUES (?, ?, 2022-10-07, 'Pretty good', TRUE)",
            (sherman_id, minh_phan_id),
        )
        cursor.execute(
            "INSERT INTO Ratings (apt_id, user_id, date_of_rating, comment, vote) \
            VALUES (?, ?, 2022-10-08, 'Bruh this sucks', FALSE)",
            (sherman_id, minh_id),
        )
        cursor.execute(
            "INSERT INTO Ratings (apt_id, user_id, date_of_rating, comment, vote) \
            VALUES (?, ?, 2022-10-09, 'Decent', TRUE)",
            (sherman_id, big_finger_id),
        )
        cursor.execute(
            "INSERT INTO Ratings (apt_id, user_id, date_of_rating, comment, vote) \
            VALUES (?, ?, 2022-10-10, 'Decent hall', TRUE)",
            (far_id, big_finger_id),
        )
        cursor.execute(
            "INSERT INTO Ratings (apt_id, user_id, date_of_rating, comment, vote) \
            VALUES (?, ?, 2022-10-11, 'Why', FALSE)",
            (par_id, big_finger_id),
        )
        connection.commit()

    def clean_up_users(self, cursor: sqlite3.Cursor, connection: sqlite3.Connection):
        """Delete users inserted during test"""
        args = [
            ("Minh Phan",),
            ("Minh",),
            ("Big_finger",),
        ]
        cursor.executemany("DELETE FROM Users WHERE username = ?", args)
        connection.commit()

    def clean_up_apartments(
        self, cursor: sqlite3.Cursor, connection: sqlite3.Connection
    ):
        """Delete apartments inserted during test"""
        args = [
            ("Sherman",),
            ("FAR",),
            ("Lincoln",),
            ("PAR",),
        ]
        cursor.executemany("DELETE FROM Apartments WHERE apt_name = ?", args)
        connection.commit()

    def clean_up_reviews(self, cursor: sqlite3.Cursor, connection: sqlite3.Connection):
        """Delete reviews inserted during test"""
        sherman_id = cursor.execute(
            "SELECT apt_id FROM Apartments WHERE (apt_name = 'Sherman')"
        ).fetchone()[0]
        far_id = cursor.execute(
            "SELECT apt_id FROM Apartments WHERE (apt_name = 'FAR')"
        ).fetchone()[0]
        par_id = cursor.execute(
            "SELECT apt_id FROM Apartments WHERE (apt_name = 'PAR')"
        ).fetchone()[0]
        args = [
            (sherman_id,),
            (far_id,),
            (par_id,),
        ]
        cursor.executemany("DELETE FROM Ratings WHERE apt_id = ?", args)
        connection.commit()

    def clean_up_pics(self, cursor: sqlite3.Cursor, connection: sqlite3.Connection):
        """Clean up pics inserted during test"""
        sherman_id = cursor.execute(
            "SELECT apt_id FROM Apartments WHERE (apt_name = 'Sherman')"
        ).fetchone()[0]
        cursor.execute("DELETE FROM AptPics WHERE apt_id = ?", (sherman_id,))
        connection.commit()

    def initialize_all(self):
        """Initialize test data"""
        connection = sqlite3.connect("database/database.db")
        cursor = connection.cursor()
        self.insert_apartments(cursor, connection)
        self.insert_users(cursor, connection)
        self.insert_reviews(cursor, connection)
        self.insert_pics(cursor, connection)
        connection.close()

    def clean_all(self):
        """Clean up test data"""
        connection = sqlite3.connect("database/database.db")
        cursor = connection.cursor()
        self.clean_up_reviews(cursor, connection)
        self.clean_up_pics(cursor, connection)
        self.clean_up_apartments(cursor, connection)
        self.clean_up_users(cursor, connection)
        connection.close()

    def test_search_apartments_invalid(self):
        """Test invalid query"""
        sample_search_apts = []

        self.initialize_all()

        res = self.main_page.search_apartments("w")

        self.clean_all()
        assert sample_search_apts == res

    def test_get_apartments_pictures_invalid(self):
        """Test get pics of invalid apartment"""
        sample_apts_picture = []

        self.initialize_all()

        connection = sqlite3.connect("database/database.db")
        cursor = connection.cursor()
        sherman_id = cursor.execute(
            "SELECT apt_id FROM Apartments WHERE (apt_name = 'Sherman')"
        ).fetchone()[0]
        connection.close()
        res = self.main_page.get_apartments_pictures(sherman_id)

        self.clean_all()
        assert sample_apts_picture == res

    def test_get_apartments_reviews_empty(self):
        """Test get reviews of invalid apartments"""
        sample_apts_review = []

        self.initialize_all()

        connection = sqlite3.connect("database/database.db")
        cursor = connection.cursor()
        sherman_id = cursor.execute(
            "SELECT apt_id FROM Apartments WHERE (apt_name = 'Sherman')"
        ).fetchone()[0]
        connection.close()
        res = self.main_page.get_apartments_reviews(sherman_id)

        self.clean_all()
        assert sample_apts_review == res