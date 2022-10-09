"""Test mainpage.py"""
import sqlite3
from mainpage import MainPage
from apt import Apt
from review import Review


class TestMainPage:
    """Test main page class"""

    main_page = MainPage()
    connection = sqlite3.connect("database/database.db")
    cursor = connection.cursor()

    def insert_apartments(self):
        """Insert apartments for use by test methods"""
        self.cursor.execute(
            "INSERT INTO Apartments (apt_name, apt_address, price_min, price_max, link) \
            VALUES (?, ?, ?, ?, ?)",
            ("Sherman", "909 S 5th St", 5500, 6500, ""),
        )
        self.cursor.execute(
            "INSERT INTO Apartments (apt_name, apt_address, price_min, price_max, link) \
            VALUES (?, ?, ?, ?, ?)",
            ("FAR", "901 W College Ct", 6000, 7000, ""),
        )
        self.cursor.execute(
            "INSERT INTO Apartments (apt_name, apt_address, price_min, price_max, link) \
            VALUES (?, ?, ?, ?, ?)",
            ("Lincoln", "1005 S Lincoln Ave", 5000, 6000, ""),
        )
        self.cursor.execute(
            "INSERT INTO Apartments (apt_name, apt_address, price_min, price_max, link) \
            VALUES (?, ?, ?, ?, ?)",
            ("PAR", "901 W College Ct", 5000, 6000, ""),
        )

    def insert_users(self):
        """Initialize users for use by test methods"""
        self.cursor.execute(
            "INSERT INTO Users (username, password, email, phone) \
            VALUES (?, ?, ?, ?, ?)",
            ("Minh Phan", "", "", ""),
        )
        self.cursor.execute(
            "INSERT INTO Users (username, password, email, phone) \
            VALUES (?, ?, ?, ?, ?)",
            ("Minh", "", "", ""),
        )
        self.cursor.execute(
            "INSERT INTO Users (username, password, email, phone) \
            VALUES (?, ?, ?, ?, ?)",
            ("Big_finger", "", "", ""),
        )

    def insert_pics(self):
        """Initialize pics for use by test methods"""
        sherman_id = self.cursor.execute(
            "SELECT apt_id FROM Apartments WHERE (apt_name = 'Sherman')"
        ).fetchone()
        self.cursor.execute(
            "INSERT INTO AptPics (apt_id, link) VALUES (?, 'Link1')", (sherman_id,)
        )
        self.cursor.execute(
            "INSERT INTO AptPics (apt_id, link) VALUES (?, 'Link2')", (sherman_id,)
        )
        self.cursor.execute(
            "INSERT INTO AptPics (apt_id, link) VALUES (?, 'Link3')", (sherman_id,)
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
        self.cursor.execute("DELETE FROM Users WHERE username = 'Minh Phan'")
        self.cursor.execute("DELETE FROM Users WHERE username = 'Minh'")
        self.cursor.execute("DELETE FROM Users WHERE username = 'Big_finger'")

    def clean_up_apartments(self):
        """Delete apartments inserted during test"""
        self.cursor.execute("DELETE FROM Apartments WHERE apt_name = 'Sherman'")
        self.cursor.execute("DELETE FROM Apartments WHERE apt_name = 'FAR'")
        self.cursor.execute("DELETE FROM Apartments WHERE apt_name = 'Lincoln'")
        self.cursor.execute("DELETE FROM Apartments WHERE apt_name = 'PAR'")

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
        self.cursor.execute("DELETE FROM Ratings WHERE apt_id = ?", (sherman_id,))
        self.cursor.execute("DELETE FROM Ratings WHERE apt_id = ?", (far_id,))
        self.cursor.execute("DELETE FROM Ratings WHERE apt_id = ?", (par_id,))

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

    def test_search_apartments(self):
        """Test search_apartment() returns correct list"""
        sample_search_apts = []
        sample_search_apts.append(Apt("FAR", "901 W College Ct", 1, (6000, 7000)))
        sample_search_apts.append(Apt("PAR", "901 W College Ct", -1, (5000, 6000)))

        self.initialize_all()
        res = self.main_page.search_apartments("ar")
        self.clean_all()
        assert sample_search_apts == res

    def test_apartments_default(self):
        """Test apartments_default() returns correct list"""
        sample_apts_default = []
        sample_apts_default.append(Apt("Sherman", "909 S 5th St", 1, [5500, 6500]))
        sample_apts_default.append(Apt("FAR", "901 W College Ct", 1, (6000, 7000)))
        sample_apts_default.append(
            Apt("Lincoln", "1005 S Lincoln Ave", 0, (5000, 6000))
        )

        self.initialize_all()
        res = self.main_page.apartments_default(3)
        self.clean_all()
        assert sample_apts_default == res

    def test_apartments_sorted_default(self):
        """Test apartments_sorted() returns correct list"""
        sample_apts_sorted = []
        sample_apts_sorted.append(Apt("Sherman", "909 S 5th St", 1, [5500, 6500]))
        sample_apts_sorted.append(Apt("FAR", "901 W College Ct", 1, (6000, 7000)))
        sample_apts_sorted.append(Apt("Lincoln", "1005 S Lincoln Ave", 0, (5000, 6000)))

        self.initialize_all()
        res = self.main_page.apartments_sorted(3, 0, 0)
        self.clean_all()
        assert sample_apts_sorted == res

    def test_apartments_sorted_rating_reversed(self):
        """Test returns list rating from low to high"""
        sample_apts_sorted = []
        sample_apts_sorted.append(Apt("PAR", "901 W College Ct", -1, (5000, 6000)))
        sample_apts_sorted.append(Apt("Lincoln", "1005 S Lincoln Ave", 0, (5000, 6000)))
        sample_apts_sorted.append(Apt("FAR", "901 W College Ct", 1, (6000, 7000)))

        self.initialize_all()
        res = self.main_page.apartments_sorted(3, 0, -1)
        self.clean_all()
        assert sample_apts_sorted == res

    def test_apartments_sorted_price_reversed(self):
        """Test returns price from low to high"""
        sample_apts_sorted = []
        sample_apts_sorted.append(Apt("Lincoln", "1005 S Lincoln Ave", 0, (5000, 6000)))
        sample_apts_sorted.append(Apt("PAR", "901 W College Ct", -1, (5000, 6000)))
        sample_apts_sorted.append(Apt("Sherman", "909 S 5th St", 1, [5500, 6500]))

        self.initialize_all()
        res = self.main_page.apartments_sorted(3, -1, 0)
        self.clean_all()
        assert sample_apts_sorted == res

    def test_apartments_sorted_price(self):
        """Test returns price from high to low"""
        sample_apts_sorted = []
        sample_apts_sorted.append(Apt("FAR", "901 W College Ct", 1, (6000, 7000)))
        sample_apts_sorted.append(Apt("Sherman", "909 S 5th St", 1, [5500, 6500]))
        sample_apts_sorted.append(Apt("Lincoln", "1005 S Lincoln Ave", 0, (5000, 6000)))

        self.initialize_all()
        res = self.main_page.apartments_sorted(3, 1, 0)
        self.clean_all()
        assert sample_apts_sorted == res

    def test_get_apartments_pictures(self):
        """Test get_apartments_picture()"""
        sample_apts_picture = ["Link1", "Link2", "Link3"]

        self.initialize_all()
        res = self.main_page.get_apartments_pictures("Sherman")
        self.clean_all()
        assert sample_apts_picture == res

    def test_get_apartments_reviews(self):
        """Test get_apartments_reviews()"""
        sample_apts_review = []
        sample_apts_review.append(
            Review("Minh Phan", "2022-10-07", "Pretty good", True)
        )
        sample_apts_review.append(
            Review("Minh", "2022-10-08", "Bruh this sucks", False)
        )
        sample_apts_review.append(Review("Big_finger", "2022-10-09", "Decent", True))

        self.initialize_all()
        res = self.main_page.get_apartments_reviews("Sherman")
        self.clean_all()
        assert sample_apts_review == res
