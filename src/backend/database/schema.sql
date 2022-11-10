DROP TABLE IF EXISTS Users;
DROP TABLE IF EXISTS Apartments;
DROP TABLE IF EXISTS AptPics;
DROP TABLE IF EXISTS Reviews;
CREATE TABLE Users (
    user_id INTEGER PRIMARY KEY AUTOINCREMENT,
    username VARCHAR(255) NOT NULL, 
    password VARCHAR(64) NOT NULL,
    email VARCHAR(64) NOT NULL,
    phone VARCHAR(20),
    apt_id INTEGER
);

CREATE TABLE Apartments (
    apt_id INTEGER PRIMARY KEY AUTOINCREMENT,
    apt_name VARCHAR(255) NOT NULL,
    apt_address VARCHAR(255),
    price_min INTEGER,
    price_max INTEGER,
    link TEXT
);

CREATE TABLE AptPics (
    apt_id INTEGER NOT NULL,
    link TEXT NOT NULL
);

CREATE TABLE Reviews (
    rating_id INTEGER PRIMARY KEY AUTOINCREMENT,
    apt_id INTEGER NOT NULL,
    user_id INTEGER NOT NULL,
    date_of_rating DATE NOT NULL,
    comment TEXT,
    vote INTEGER CHECK(vote = 1 OR vote = 0 OR vote = -1),
    UNIQUE(apt_id, user_id)
);

-- TEST
INSERT INTO Users (username, password, email, phone, apt_id)
VALUES ('Zongxian', '12345abcde', 'Zongxian@Feng.com', '1234567890', 1);

INSERT INTO Users (username, password, email, phone, apt_id)
VALUES ('MonteCarlo', 'qwert#6767', 'Monte@Carlo.com', '9876543210', 2);

INSERT INTO Users (username, password, email, phone, apt_id)
VALUES ('Minh', 'hello123', 'Minh.com', '9876543210', 2);

INSERT INTO Apartments (apt_name, apt_address, price_min, price_max, link)
VALUES ('The Dean Campustown', '708 S 6th St, Champaign, IL 61820', 860, 1900, 'https://www.apartmentfinder.com/Illinois/Champaign-Apartments/The-Dean-Campustown-Apartments-ttrtct8');

INSERT INTO Apartments (apt_name, apt_address, price_min, price_max, link)
VALUES ('Seven07 Apartments', '707 S 4th St, Champaign, IL 61820', 856, 1750, 'https://www.apartmentfinder.com/Illinois/Champaign-Apartments/Seven07-Apartments-75ckgzx');

<<<<<<< HEAD
INSERT INTO AptPics (apt_id, link)
VALUES (2, 'https://image1.apartmentfinder.com/i2/yI_vOGHFLSjSR7fuXTtN6vEcPux3OoeLbY-pKtkIda8/116/seven07-champaign-il-4-br-4-ba---living-room.jpg');
=======
-- INSERT INTO AptPics (apt_id, link)
-- VALUES (1, 'https://image1.apartmentfinder.com/i2/yI_vOGHFLSjSR7fuXTtN6vEcPux3OoeLbY-pKtkIda8/116/seven07-champaign-il-4-br-4-ba---living-room.jpg');
>>>>>>> f1bfa98339d10778892fa18c6638d635a0bf4f96

INSERT INTO AptPics (apt_id, link)
VALUES (2, 'https://image1.apartmentfinder.com/i2/fU58gLkELEv-9Yoe6T4cecz5HcARTNYp-eA3RtF1wY0/116/seven07-champaign-il-building-photo.jpg');

INSERT INTO Reviews (apt_id, user_id, date_of_rating, comment, vote)
VALUES (1, 1, '2021-09-23', 'Great Apartment, I love it!', 1);

INSERT INTO Reviews (apt_id, user_id, date_of_rating, comment, vote)
VALUES (2, 2, '2021-09-23', 'Shit Apartment, I hate it!', -1);


