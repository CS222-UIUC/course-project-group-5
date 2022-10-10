"""Test mainpage.py invalid calls"""
import sqlite3
from mainpage import MainPage


class TestMainPageInvalid:
    """Test invalid calls to MainPage methods"""

    main_page = MainPage()
    connection = sqlite3.connect("database/database.db")
    cursor = connection.cursor()

    def insert_apartments(self):
        """Insert apartments for use by test methods"""
        args = [
            ("Sherman", "909 S 5th St", 5500, 6500, ""),
            ("FAR", "901 W College Ct", 6000, 7000, ""),
            ("Lincoln", "1005 S Lincoln Ave", 5000, 6000, ""),
            ("PAR", "901 W College Ct", 5000, 6000, ""),
        ]
        self.cursor.executemany(
            "INSERT INTO Apartments (apt_name, apt_address, price_min, price_max, link) \
            VALUES (?, ?, ?, ?, ?)",
            args,
        )

    def insert_users(self):
        """Initialize users for use by test methods"""
        args = [
            ("Minh Phan", "", "", ""),
            ("Minh", "", "", ""),
            ("Big_finger", "", "", ""),
        ]
        self.cursor.executemany(
            "INSERT INTO Users (username, password, email, phone) \
            VALUES (?, ?, ?, ?)",
            args,
        )

    def insert_pics(self):
        """Initialize pics for use by test methods"""
        sherman_id = self.cursor.execute(
            "SELECT apt_id FROM Apartments WHERE (apt_name = 'Sherman')"
        ).fetchone()
        args_link = ["Link1", "Link2", "Link3"]
        self.cursor.executemany(
            "INSERT INTO AptPics (apt_id, link) VALUES (?, ?)", (sherman_id, args_link)
        )

    def insert_reviews(self):
        """Initialize reviews for use by test methods"""
        sherman_id = self.cursor.execute(
            "SELECT apt_id FROM Apartments WHERE (apt_name = 'Sherman')"
        ).fetchone()
        far_id = self.cursor.execute(
            "SELECT apt_id FROM Apartments WHERE (apt_name = 'FAR')"
        ).fetchone()
        par_id = self.cursor.execute(
            "SELECT apt_id FROM Apartments WHERE (apt_name = 'PAR')"
        ).fetchone()
        minh_phan_id = self.cursor.execute(
            "SELECT user_id FROM Users WHERE (username = 'Minh Phan')"
        ).fetchone()
        minh_id = self.cursor.execute(
            "SELECT user_id FROM Users WHERE (username = 'Minh')"
        ).fetchone()
        big_finger_id = self.cursor.execute(
            "SELECT user_id FROM Users WHERE (username = 'Big_finger')"
        ).fetchone()
        self.cursor.execute(
            "INSERT INTO Ratings (apt_id, user_id, date_of_rating, comment, vote) \
            VALUES (?, ?, 2022-10-07, 'Pretty good', TRUE)",
            (sherman_id, minh_phan_id),
        )
        self.cursor.execute(
            "INSERT INTO Ratings (apt_id, user_id, date_of_rating, comment, vote) \
            VALUES (?, ?, 2022-10-08, 'Bruh this sucks', FALSE)",
            (sherman_id, minh_id),
        )
        self.cursor.execute(
            "INSERT INTO Ratings (apt_id, user_id, date_of_rating, comment, vote) \
            VALUES (?, ?, 2022-10-09, 'Decent', TRUE)",
            (sherman_id, big_finger_id),
        )
        self.cursor.execute(
            "INSERT INTO Ratings (apt_id, user_id, date_of_rating, comment, vote) \
            VALUES (?, ?, 2022-10-10, 'Decent hall', TRUE)",
            (far_id, big_finger_id),
        )
        self.cursor.execute(
            "INSERT INTO Ratings (apt_id, user_id, date_of_rating, comment, vote) \
            VALUES (?, ?, 2022-10-11, 'Why', FALSE)",
            (par_id, big_finger_id),
        )

    def clean_up_users(self):
        """Delete users inserted during test"""
        args = [
            ("Minh Phan",),
            ("Minh",),
            ("Big_finger",),
        ]
        self.cursor.executescript("DELETE FROM Users WHERE username = ?", args)

    def clean_up_apartments(self):
        """Delete apartments inserted during test"""
        args = [
            ("Sherman",),
            ("FAR",),
            ("Lincoln",),
            ("PAR",),
        ]
        self.cursor.executescript("DELETE FROM Apartments WHERE apt_name = ?", args)

    def clean_up_reviews(self):
        """Delete reviews inserted during test"""
        sherman_id = self.cursor.execute(
            "SELECT apt_id FROM Apartments WHERE (apt_name = 'Sherman')"
        ).fetchone()
        far_id = self.cursor.execute(
            "SELECT apt_id FROM Apartments WHERE (apt_name = 'FAR')"
        ).fetchone()
        par_id = self.cursor.execute(
            "SELECT apt_id FROM Apartments WHERE (apt_name = 'PAR')"
        ).fetchone()
        args = [
            (sherman_id,),
            (far_id,),
            (par_id,),
        ]
        self.cursor.executemany("DELETE FROM Ratings WHERE apt_id = ?", args)

    def clean_up_pics(self):
        """Clean up pics inserted during test"""
        sherman_id = self.cursor.execute(
            "SELECT apt_id FROM Apartments WHERE (apt_name = 'Sherman')"
        ).fetchone()
        self.cursor.execute("DELETE FROM AptPics WHERE apt_id = ?", (sherman_id,))

    def initialize_all(self):
        """Initialize test data"""
        self.insert_apartments()
        self.insert_users()
        self.insert_reviews()
        self.insert_pics()

    def clean_all(self):
        """Clean up test data"""
        self.clean_up_reviews()
        self.clean_up_pics()
        self.clean_up_apartments()
        self.insert_users()

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
        res = self.main_page.get_apartments_pictures("Daniels")
        self.clean_all()
        assert sample_apts_picture == res

    def test_get_apartments_reviews_empty(self):
        """Test get reviews of invalid apartments"""
        sample_apts_review = []

        self.initialize_all()
        res = self.main_page.get_apartments_reviews("Daniels")
        self.clean_all()
        assert sample_apts_review == res
