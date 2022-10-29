"""Test mainpage.py"""
import sqlite3
from datetime import date
from mainpage import MainPage
from apt import Apt
from review import Review
from tests.mainpage_staging import MainPageStaging


class TestMainPage:
    """Test main page class"""

    main_page = MainPage()
    main_page_stage = MainPageStaging()

    def test_search_apartments(self):
        """Test search_apartment() returns correct list"""
        self.main_page_stage.initialize_all()

        connection = sqlite3.connect("database/database.db")
        cursor = connection.cursor()
        sherman_id = cursor.execute(
            "SELECT apt_id FROM Apartments WHERE (apt_name = 'Sherman')"
        ).fetchone()[0]
        connection.close()
        sample_search_apts = []
        sample_search_apts.append(
            Apt(sherman_id, "Sherman", "909 S 5th St", 1, 5500, 6500)
        )

        res = self.main_page.search_apartments("sherma")

        self.main_page_stage.clean_all()
        assert sample_search_apts == res

    def test_apartments_default(self):
        """Test apartments_default() returns correct list"""
        self.main_page_stage.initialize_all()

        connection = sqlite3.connect("database/database.db")
        cursor = connection.cursor()
        sherman_id = cursor.execute(
            "SELECT apt_id FROM Apartments WHERE (apt_name = 'Sherman')"
        ).fetchone()[0]
        isr_id = cursor.execute(
            "SELECT apt_id FROM Apartments WHERE (apt_name = 'ISR')"
        ).fetchone()[0]
        far_id = cursor.execute(
            "SELECT apt_id FROM Apartments WHERE (apt_name = 'FAR')"
        ).fetchone()[0]
        connection.close()
        sample_apts_default = []
        sample_apts_default.append(
            Apt(far_id, "FAR", "901 W College Ct", 1, 6000, 7000)
        )
        sample_apts_default.append(
            Apt(sherman_id, "Sherman", "909 S 5th St", 1, 5500, 6500)
        )
        sample_apts_default.append(Apt(isr_id, "ISR", "918 W Illinois", 0, 6000, 7000))

        res = self.main_page.apartments_default(3)

        self.main_page_stage.clean_all()
        assert sample_apts_default == res

    def test_apartments_sorted_default(self):
        """Test apartments_sorted() returns correct list"""
        self.main_page_stage.initialize_all()

        connection = sqlite3.connect("database/database.db")
        cursor = connection.cursor()
        sherman_id = cursor.execute(
            "SELECT apt_id FROM Apartments WHERE (apt_name = 'Sherman')"
        ).fetchone()[0]
        isr_id = cursor.execute(
            "SELECT apt_id FROM Apartments WHERE (apt_name = 'ISR')"
        ).fetchone()[0]
        far_id = cursor.execute(
            "SELECT apt_id FROM Apartments WHERE (apt_name = 'FAR')"
        ).fetchone()[0]
        connection.close()
        sample_apts_sorted = []
        sample_apts_sorted.append(Apt(far_id, "FAR", "901 W College Ct", 1, 6000, 7000))
        sample_apts_sorted.append(
            Apt(sherman_id, "Sherman", "909 S 5th St", 1, 5500, 6500)
        )
        sample_apts_sorted.append(Apt(isr_id, "ISR", "918 W Illinois", 0, 6000, 7000))

        res = self.main_page.apartments_sorted(3, 0, 0)

        self.main_page_stage.clean_all()
        assert sample_apts_sorted == res

    def test_apartments_sorted_rating_reversed(self):
        """Test returns list rating from low to high"""
        self.main_page_stage.initialize_all()

        connection = sqlite3.connect("database/database.db")
        cursor = connection.cursor()
        par_id = cursor.execute(
            "SELECT apt_id FROM Apartments WHERE (apt_name = 'PAR')"
        ).fetchone()[0]
        isr_id = cursor.execute(
            "SELECT apt_id FROM Apartments WHERE (apt_name = 'ISR')"
        ).fetchone()[0]
        lincoln_id = cursor.execute(
            "SELECT apt_id FROM Apartments WHERE (apt_name = 'Lincoln')"
        ).fetchone()[0]
        connection.close()
        sample_apts_sorted = []
        sample_apts_sorted.append(
            Apt(par_id, "PAR", "901 W College Ct", -1, 5000, 6000)
        )
        sample_apts_sorted.append(Apt(isr_id, "ISR", "918 W Illinois", 0, 6000, 7000))
        sample_apts_sorted.append(
            Apt(lincoln_id, "Lincoln", "1005 S Lincoln Ave", 0, 5000, 6000)
        )

        res = self.main_page.apartments_sorted(3, 0, -1)

        self.main_page_stage.clean_all()
        assert sample_apts_sorted == res

    def test_apartments_sorted_price_reversed(self):
        """Test returns price from low to high"""
        self.main_page_stage.initialize_all()

        connection = sqlite3.connect("database/database.db")
        cursor = connection.cursor()
        lincoln_id = cursor.execute(
            "SELECT apt_id FROM Apartments WHERE (apt_name = 'Lincoln')"
        ).fetchone()[0]
        par_id = cursor.execute(
            "SELECT apt_id FROM Apartments WHERE (apt_name = 'PAR')"
        ).fetchone()[0]
        sherman_id = cursor.execute(
            "SELECT apt_id FROM Apartments WHERE (apt_name = 'Sherman')"
        ).fetchone()[0]
        connection.close()
        sample_apts_sorted = []
        sample_apts_sorted.append(
            Apt(lincoln_id, "Lincoln", "1005 S Lincoln Ave", 0, 5000, 6000)
        )
        sample_apts_sorted.append(
            Apt(par_id, "PAR", "901 W College Ct", -1, 5000, 6000)
        )
        sample_apts_sorted.append(
            Apt(sherman_id, "Sherman", "909 S 5th St", 1, 5500, 6500)
        )

        res = self.main_page.apartments_sorted(3, -1, 0)

        self.main_page_stage.clean_all()
        assert sample_apts_sorted == res

    def test_apartments_sorted_price(self):
        """Test returns price from high to low"""
        self.main_page_stage.initialize_all()

        connection = sqlite3.connect("database/database.db")
        cursor = connection.cursor()
        sherman_id = cursor.execute(
            "SELECT apt_id FROM Apartments WHERE (apt_name = 'Sherman')"
        ).fetchone()[0]
        isr_id = cursor.execute(
            "SELECT apt_id FROM Apartments WHERE (apt_name = 'ISR')"
        ).fetchone()[0]
        far_id = cursor.execute(
            "SELECT apt_id FROM Apartments WHERE (apt_name = 'FAR')"
        ).fetchone()[0]
        connection.close()
        sample_apts_sorted = []
        sample_apts_sorted.append(Apt(far_id, "FAR", "901 W College Ct", 1, 6000, 7000))
        sample_apts_sorted.append(Apt(isr_id, "ISR", "918 W Illinois", 0, 6000, 7000))
        sample_apts_sorted.append(
            Apt(sherman_id, "Sherman", "909 S 5th St", 1, 5500, 6500)
        )

        res = self.main_page.apartments_sorted(3, 1, 0)

        self.main_page_stage.clean_all()
        assert sample_apts_sorted == res

    def test_apartments_sorted_price_rating_reversed(self):
        """
        Test price from high to low
        and rating from low to high
        """
        self.main_page_stage.initialize_all()

        connection = sqlite3.connect("database/database.db")
        cursor = connection.cursor()
        sherman_id = cursor.execute(
            "SELECT apt_id FROM Apartments WHERE (apt_name = 'Sherman')"
        ).fetchone()[0]
        isr_id = cursor.execute(
            "SELECT apt_id FROM Apartments WHERE (apt_name = 'ISR')"
        ).fetchone()[0]
        far_id = cursor.execute(
            "SELECT apt_id FROM Apartments WHERE (apt_name = 'FAR')"
        ).fetchone()[0]
        connection.close()
        sample_apts_sorted = []
        sample_apts_sorted.append(Apt(isr_id, "ISR", "918 W Illinois", 0, 6000, 7000))
        sample_apts_sorted.append(Apt(far_id, "FAR", "901 W College Ct", 1, 6000, 7000))
        sample_apts_sorted.append(
            Apt(sherman_id, "Sherman", "909 S 5th St", 1, 5500, 6500)
        )

        res = self.main_page.apartments_sorted(3, 1, -1)

        self.main_page_stage.clean_all()
        assert sample_apts_sorted == res

    def test_apartments_sorted_price_reversed_rating(self):
        """
        Test price from low to high
        and rating from high to low
        """
        self.main_page_stage.initialize_all()

        connection = sqlite3.connect("database/database.db")
        cursor = connection.cursor()
        lincoln_id = cursor.execute(
            "SELECT apt_id FROM Apartments WHERE (apt_name = 'Lincoln')"
        ).fetchone()[0]
        par_id = cursor.execute(
            "SELECT apt_id FROM Apartments WHERE (apt_name = 'PAR')"
        ).fetchone()[0]
        sherman_id = cursor.execute(
            "SELECT apt_id FROM Apartments WHERE (apt_name = 'Sherman')"
        ).fetchone()[0]
        connection.close()
        sample_apts_sorted = []
        sample_apts_sorted.append(
            Apt(lincoln_id, "Lincoln", "1005 S Lincoln Ave", 0, 5000, 6000)
        )
        sample_apts_sorted.append(
            Apt(par_id, "PAR", "901 W College Ct", -1, 5000, 6000)
        )
        sample_apts_sorted.append(
            Apt(sherman_id, "Sherman", "909 S 5th St", 1, 5500, 6500)
        )

        res = self.main_page.apartments_sorted(3, -1, 1)

        self.main_page_stage.clean_all()
        assert sample_apts_sorted == res

    def test_get_apartments_pictures(self):
        """Test get_apartments_picture()"""
        sample_apts_picture = ["Link1", "Link2", "Link3"]

        self.main_page_stage.initialize_all()

        connection = sqlite3.connect("database/database.db")
        cursor = connection.cursor()
        sherman_id = cursor.execute(
            "SELECT apt_id FROM Apartments WHERE (apt_name = 'Sherman')"
        ).fetchone()[0]
        connection.close()
        res = self.main_page.get_apartments_pictures(sherman_id)

        self.main_page_stage.clean_all()
        assert sample_apts_picture == res

    def test_write_apartment_review(self):
        """Test write_apartment_review()"""
        self.main_page_stage.initialize_all()
        sample_comment = "Bruh this really sucks"
        connection = sqlite3.connect("database/database.db")
        cursor = connection.cursor()
        sherman_id = cursor.execute(
            "SELECT apt_id FROM Apartments WHERE (apt_name = 'Sherman')"
        ).fetchone()[0]
        today = date.today().strftime("%Y-%m-%d")
        connection.close()
        write_result = self.main_page.write_apartment_review(
            sherman_id, "Fig_binger", sample_comment, -1
        )
        sample_apts_review = []
        sample_apts_review.append(Review("Fig_binger", today, sample_comment, False))
        sample_apts_review.append(Review("Big_finger", "2022-10-09", "Decent", True))
        sample_apts_review.append(
            Review("Minh", "2022-10-08", "Bruh this sucks", False)
        )
        sample_apts_review.append(
            Review("Minh Phan", "2022-10-07", "Pretty good", True)
        )
        self.main_page_stage.clean_all()
        assert write_result == sample_apts_review

    def test_get_apartments_reviews(self):
        """Test get_apartments_reviews()"""
        sample_apts_review = []
        sample_apts_review.append(Review("Big_finger", "2022-10-09", "Decent", True))
        sample_apts_review.append(
            Review("Minh", "2022-10-08", "Bruh this sucks", False)
        )
        sample_apts_review.append(
            Review("Minh Phan", "2022-10-07", "Pretty good", True)
        )

        self.main_page_stage.initialize_all()

        connection = sqlite3.connect("database/database.db")
        cursor = connection.cursor()
        sherman_id = cursor.execute(
            "SELECT apt_id FROM Apartments WHERE (apt_name = 'Sherman')"
        ).fetchone()[0]
        connection.close()
        res = self.main_page.get_apartments_reviews(sherman_id)

        self.main_page_stage.clean_all()
        assert sample_apts_review == res

    def test_search_apartments_invalid(self):
        """Test invalid query"""
        sample_search_apts = []

        self.main_page_stage.initialize_all()

        res = self.main_page.search_apartments("wtf")

        self.main_page_stage.clean_all()
        assert sample_search_apts == res

    def test_get_apartments_pictures_invalid(self):
        """Test get pics of invalid apartment"""
        sample_apts_picture = []

        self.main_page_stage.initialize_all()

        connection = sqlite3.connect("database/database.db")
        cursor = connection.cursor()
        sherman_id = cursor.execute(
            "SELECT apt_id FROM Apartments WHERE (apt_name = 'Sherman')"
        ).fetchone()[0]
        self.main_page_stage.clean_up_pics(cursor, connection)
        connection.close()
        res = self.main_page.get_apartments_pictures(sherman_id)

        self.main_page_stage.clean_all()
        assert sample_apts_picture == res

    def test_get_apartments_reviews_empty(self):
        """Test get reviews of invalid apartments"""
        sample_apts_review = []
        self.main_page_stage.initialize_all()
        connection = sqlite3.connect("database/database.db")
        cursor = connection.cursor()
        sherman_id = cursor.execute(
            "SELECT apt_id FROM Apartments WHERE (apt_name = 'Sherman')"
        ).fetchone()[0]
        self.main_page_stage.clean_up_reviews(cursor, connection)
        connection.close()
        res = self.main_page.get_apartments_reviews(sherman_id)
        self.main_page_stage.clean_all()
        assert sample_apts_review == res
