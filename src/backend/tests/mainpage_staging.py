"""Stage the database for"""
import sqlite3
from decorators import use_database


class MainPageStaging:
    """Stage main page data for tests"""

    def insert_apartments(self, cursor: sqlite3.Cursor, connection: sqlite3.Connection):
        """Insert apartments for use by test methods"""
        args = [
            ("Sherman", "909 S 5th St", 5500, 6500, ""),
            ("FAR", "901 W College Ct", 6000, 7000, ""),
            ("PAR", "901 W College Ct", 5000, 6000, ""),
            ("Lincoln", "1005 S Lincoln Ave", 5000, 6000, ""),
            ("ISR", "918 W Illinois", 6000, 7000, ""),
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
            ("Fig_binger", "", "", ""),
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
        args = [
            (sherman_id, minh_phan_id, "2022-10-07", "Pretty good", 1),
            (sherman_id, minh_id, "2022-10-08", "Bruh this sucks", -1),
            (sherman_id, big_finger_id, "2022-10-09", "Decent", 1),
            (far_id, big_finger_id, "2022-10-10", "Decent hall", 1),
            (par_id, big_finger_id, "2022-10-11", "Why", -1),
        ]
        cursor.executemany(
            "INSERT INTO Reviews (apt_id, user_id, date_of_rating, comment, vote) \
            VALUES (?, ?, ?, ?, ?)",
            args,
        )
        connection.commit()

    def clean_up_users(self, cursor: sqlite3.Cursor, connection: sqlite3.Connection):
        """Delete users inserted during test"""
        args = [("Minh Phan",), ("Minh",), ("Big_finger",), ("Fig_binger",)]
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
            ("ISR",),
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
        cursor.executemany("DELETE FROM Reviews WHERE apt_id = ?", args)
        connection.commit()

    def clean_up_pics(self, cursor: sqlite3.Cursor, connection: sqlite3.Connection):
        """Clean up pics inserted during test"""
        sherman_id = cursor.execute(
            "SELECT apt_id FROM Apartments WHERE (apt_name = 'Sherman')"
        ).fetchone()[0]
        cursor.execute("DELETE FROM AptPics WHERE apt_id = ?", (sherman_id,))
        connection.commit()

    @use_database
    def initialize_all(self):
        """Initialize test data"""
        conn = self.initialize_all.connection
        cur = self.initialize_all.cursor
        self.insert_apartments(cur, conn)
        self.insert_users(cur, conn)
        self.insert_reviews(cur, conn)
        self.insert_pics(cur, conn)

    @use_database
    def clean_all(self):
        """Clean up test data"""
        conn = self.initialize_all.connection
        cur = self.initialize_all.cursor
        self.clean_up_reviews(cur, conn)
        self.clean_up_pics(cur, conn)
        self.clean_up_apartments(cur, conn)
        self.clean_up_users(cur, conn)
