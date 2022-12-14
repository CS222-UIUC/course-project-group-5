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
/*
INSERT INTO Users (user_id, username, password, email, phone, apt_id)
VALUES (1, 'Zongxian', '12345abcde', 'Zongxian@Feng.com', '1234567890', 1);

INSERT INTO Users (user_id, username, password, email, phone, apt_id)
VALUES (2, 'MonteCarlo', 'qwert#6767', 'Monte@Carlo.com', '9876543210', 2);

INSERT INTO Users (user_id, username, password, email, phone, apt_id)
VALUES (3, 'Evans', 'asd', 'Evans.com', '9876543210', 3);

INSERT INTO Users (user_id, username, password, email, phone, apt_id)
VALUES (4, 'Xi', 'abcdefg', 'Monte@Carlo.com', '9876543210', 4);

INSERT INTO Users (user_id, username, password, email, phone, apt_id)
VALUES (5, 'Waterbottle', 'hello123', 'Minh.com', '9876543210', 5);

INSERT INTO Users (user_id, username, password, email, phone, apt_id)
VALUES (6, 'Pencil', 'qw??DASFD@$!@767', 'Monte@Carlo.com', '9876543210', 6);

INSERT INTO Users (user_id, username, password, email, phone, apt_id)
VALUES (7, 'Green alien', '1234324324fgrerw?$#@%?', 'Minh.com', '9876543210', 7);

INSERT INTO Users (user_id, username, password, email, phone, apt_id)
VALUES (8, 'Jefferson', '0q4043jtqwt?$#T', 'Monte@hello.com', '123456789', 8);

INSERT INTO Users (user_id, username, password, email, phone, apt_id)
VALUES (9, 'Timothy', 'asdfsdf', 'Minh.com', '9876543210', 2);

INSERT INTO Apartments (apt_id, apt_name, apt_address, price_min, price_max, link)
VALUES (1, 'The Dean Campustown', '708 S 6th St Champaign, IL 61820', 860, 1900, 'https://www.apartmentfinder.com/Illinois/Champaign-Apartments/The-Dean-Campustown-Apartments-ttrtct8');

INSERT INTO Apartments (apt_id, apt_name, apt_address, price_min, price_max, link)
VALUES (2, 'Seven07 Apartments', '707 S 4th St Champaign, IL 61820', 856, 1750, 'https://www.apartmentfinder.com/Illinois/Champaign-Apartments/Seven07-Apartments-75ckgzx');

INSERT INTO Apartments (apt_id, apt_name, apt_address, price_min, price_max, link)
VALUES (3, 'Maywood Apartments', '707 Left St Urbana, IL 61801', 300, 900, 'https://www.apartmentfinder.com/Illinois/Champaign-Apartments/The-Dean-Campustown-Apartments-ttrtct8');

INSERT INTO Apartments (apt_id, apt_name, apt_address, price_min, price_max, link)
VALUES (4, 'Champaign Park', '2106 W White St Champaign, IL 61820', 856, 1750, 'https://www.apartmentfinder.com/Illinois/Champaign-Apartments/Seven07-Apartments-75ckgzx');

INSERT INTO Apartments (apt_id, apt_name, apt_address, price_min, price_max, link)
VALUES (5, 'Capstone Quarters', '708 S 6th St Champaign, IL 61820', 860, 1900, 'https://www.apartmentfinder.com/Illinois/Champaign-Apartments/The-Dean-Campustown-Apartments-ttrtct8');

INSERT INTO Apartments (apt_id, apt_name, apt_address, price_min, price_max, link)
VALUES (6, 'Legacy202', '1234 Sunshine Ct Champaign, IL 61820', 856, 1750, 'https://www.apartmentfinder.com/Illinois/Champaign-Apartments/Seven07-Apartments-75ckgzx');

INSERT INTO Apartments (apt_id, apt_name, apt_address, price_min, price_max, link)
VALUES (7, 'Cool Apartments', '689 N 1st St Champaign, IL 61820', 435, 54635, 'https://www.apartmentfinder.com/Illinois/Champaign-Apartments/The-Dean-Campustown-Apartments-ttrtct8');

INSERT INTO Apartments (apt_id, apt_name, apt_address, price_min, price_max, link)
VALUES (8, 'Luxury Student Housing', '710 S 4th St Champaign, IL 61820', 233, 444, 'https://www.apartmentfinder.com/Illinois/Champaign-Apartments/Seven07-Apartments-75ckgzx');

INSERT INTO Apartments (apt_id, apt_name, apt_address, price_min, price_max, link)
VALUES (9, 'House', '708 S 6th St Champaign, IL 61820', 5, 45, 'https://www.apartmentfinder.com/Illinois/Champaign-Apartments/The-Dean-Campustown-Apartments-ttrtct8');

INSERT INTO Apartments (apt_id, apt_name, apt_address, price_min, price_max, link)
VALUES (10, 'Fields South', '3301 Fields South St Champaign, IL 61820', 345, 4536, 'https://www.apartmentfinder.com/Illinois/Champaign-Apartments/Seven07-Apartments-75ckgzx');

INSERT INTO Apartments (apt_id, apt_name, apt_address, price_min, price_max, link)
VALUES (11, 'An Apartment', '1600 W Bradley St Champaign, IL 61820', 21, 346346, 'https://www.apartmentfinder.com/Illinois/Champaign-Apartments/The-Dean-Campustown-Apartments-ttrtct8');

INSERT INTO Apartments (apt_id, apt_name, apt_address, price_min, price_max, link)
VALUES (12, 'Skyline Tower', '519 E Green St Champaign, IL 61820', 2323, 12345, 'https://www.apartmentfinder.com/Illinois/Champaign-Apartments/Seven07-Apartments-75ckgzx');

INSERT INTO Apartments (apt_id, apt_name, apt_address, price_min, price_max, link)
VALUES (13, 'Baytowne Apartments', '1000 Baytowne Dr Champaign, IL 61820', 345, 555, 'https://www.apartmentfinder.com/Illinois/Champaign-Apartments/The-Dean-Campustown-Apartments-ttrtct8');

INSERT INTO Apartments (apt_id, apt_name, apt_address, price_min, price_max, link)
VALUES (14, 'Fields South', '3301 Fields South St Champaign, IL 61820', 666, 777, 'https://www.apartmentfinder.com/Illinois/Champaign-Apartments/Seven07-Apartments-75ckgzx');

INSERT INTO Apartments (apt_id, apt_name, apt_address, price_min, price_max, link)
VALUES (15, 'Westgate Apartments', '1600 W Bradley St Champaign, IL 61820', 555, 654, 'https://www.apartmentfinder.com/Illinois/Champaign-Apartments/The-Dean-Campustown-Apartments-ttrtct8');

INSERT INTO Apartments (apt_id, apt_name, apt_address, price_min, price_max, link)
VALUES (16, '112 Green', '112 E Green St Champaign, IL 61820', 123, 234, 'https://www.apartmentfinder.com/Illinois/Champaign-Apartments/Seven07-Apartments-75ckgzx');

INSERT INTO Apartments (apt_id, apt_name, apt_address, price_min, price_max, link)
VALUES (17, 'Hunters Pond Apartment Homes', '2717 Hunters Pand Run Champaign, IL 61820', 555, 778, 'https://www.apartmentfinder.com/Illinois/Champaign-Apartments/The-Dean-Campustown-Apartments-ttrtct8');

INSERT INTO Apartments (apt_id, apt_name, apt_address, price_min, price_max, link)
VALUES (18, 'Fields South', '3301 Fields South St Champaign, IL 61820', 998, 999, 'https://www.apartmentfinder.com/Illinois/Champaign-Apartments/Seven07-Apartments-75ckgzx');

INSERT INTO Apartments (apt_id, apt_name, apt_address, price_min, price_max, link)
VALUES (19, 'Westgate Apartments', '1600 W Bradley St Champaign, IL 61820', 21, 346346, 'https://www.apartmentfinder.com/Illinois/Champaign-Apartments/The-Dean-Campustown-Apartments-ttrtct8');

INSERT INTO Apartments (apt_id, apt_name, apt_address, price_min, price_max, link)
VALUES (20, '112 Green', '112 E Green St Champaign, IL 61820', 900, 2314, 'https://www.apartmentfinder.com/Illinois/Champaign-Apartments/Seven07-Apartments-75ckgzx');

INSERT INTO AptPics (apt_id, link)
VALUES (1, 'https://image1.apartmentfinder.com/i2/yI_vOGHFLSjSR7fuXTtN6vEcPux3OoeLbY-pKtkIda8/116/seven07-champaign-il-4-br-4-ba---living-room.jpg');

INSERT INTO AptPics (apt_id, link)
VALUES (2, 'https://image1.apartmentfinder.com/i2/fU58gLkELEv-9Yoe6T4cecz5HcARTNYp-eA3RtF1wY0/116/seven07-champaign-il-building-photo.jpg');

INSERT INTO AptPics (apt_id, link)
VALUES (3, 'https://image1.apartmentfinder.com/i2/yI_vOGHFLSjSR7fuXTtN6vEcPux3OoeLbY-pKtkIda8/116/seven07-champaign-il-4-br-4-ba---living-room.jpg');

INSERT INTO AptPics (apt_id, link)
VALUES (4, 'https://image1.apartmentfinder.com/i2/fU58gLkELEv-9Yoe6T4cecz5HcARTNYp-eA3RtF1wY0/116/seven07-champaign-il-building-photo.jpg');

INSERT INTO AptPics (apt_id, link)
VALUES (5, 'https://image1.apartmentfinder.com/i2/yI_vOGHFLSjSR7fuXTtN6vEcPux3OoeLbY-pKtkIda8/116/seven07-champaign-il-4-br-4-ba---living-room.jpg');

INSERT INTO AptPics (apt_id, link)
VALUES (6, 'https://image1.apartmentfinder.com/i2/fU58gLkELEv-9Yoe6T4cecz5HcARTNYp-eA3RtF1wY0/116/seven07-champaign-il-building-photo.jpg');

INSERT INTO AptPics (apt_id, link)
VALUES (7, 'https://image1.apartmentfinder.com/i2/yI_vOGHFLSjSR7fuXTtN6vEcPux3OoeLbY-pKtkIda8/116/seven07-champaign-il-4-br-4-ba---living-room.jpg');

INSERT INTO AptPics (apt_id, link)
VALUES (8, 'https://image1.apartmentfinder.com/i2/fU58gLkELEv-9Yoe6T4cecz5HcARTNYp-eA3RtF1wY0/116/seven07-champaign-il-building-photo.jpg');

INSERT INTO AptPics (apt_id, link)
VALUES (9, 'https://image1.apartmentfinder.com/i2/yI_vOGHFLSjSR7fuXTtN6vEcPux3OoeLbY-pKtkIda8/116/seven07-champaign-il-4-br-4-ba---living-room.jpg');

INSERT INTO AptPics (apt_id, link)
VALUES (10, 'https://image1.apartmentfinder.com/i2/fU58gLkELEv-9Yoe6T4cecz5HcARTNYp-eA3RtF1wY0/116/seven07-champaign-il-building-photo.jpg');

INSERT INTO AptPics (apt_id, link)
VALUES (11, 'https://image1.apartmentfinder.com/i2/yI_vOGHFLSjSR7fuXTtN6vEcPux3OoeLbY-pKtkIda8/116/seven07-champaign-il-4-br-4-ba---living-room.jpg');

INSERT INTO AptPics (apt_id, link)
VALUES (12, 'https://image1.apartmentfinder.com/i2/fU58gLkELEv-9Yoe6T4cecz5HcARTNYp-eA3RtF1wY0/116/seven07-champaign-il-building-photo.jpg');

INSERT INTO AptPics (apt_id, link)
VALUES (13, 'https://image1.apartmentfinder.com/i2/yI_vOGHFLSjSR7fuXTtN6vEcPux3OoeLbY-pKtkIda8/116/seven07-champaign-il-4-br-4-ba---living-room.jpg');

INSERT INTO AptPics (apt_id, link)
VALUES (14, 'https://image1.apartmentfinder.com/i2/fU58gLkELEv-9Yoe6T4cecz5HcARTNYp-eA3RtF1wY0/116/seven07-champaign-il-building-photo.jpg');

INSERT INTO AptPics (apt_id, link)
VALUES (15, 'https://image1.apartmentfinder.com/i2/yI_vOGHFLSjSR7fuXTtN6vEcPux3OoeLbY-pKtkIda8/116/seven07-champaign-il-4-br-4-ba---living-room.jpg');

INSERT INTO AptPics (apt_id, link)
VALUES (16, 'https://image1.apartmentfinder.com/i2/fU58gLkELEv-9Yoe6T4cecz5HcARTNYp-eA3RtF1wY0/116/seven07-champaign-il-building-photo.jpg');

INSERT INTO AptPics (apt_id, link)
VALUES (17, 'https://image1.apartmentfinder.com/i2/yI_vOGHFLSjSR7fuXTtN6vEcPux3OoeLbY-pKtkIda8/116/seven07-champaign-il-4-br-4-ba---living-room.jpg');

INSERT INTO AptPics (apt_id, link)
VALUES (18, 'https://image1.apartmentfinder.com/i2/fU58gLkELEv-9Yoe6T4cecz5HcARTNYp-eA3RtF1wY0/116/seven07-champaign-il-building-photo.jpg');

INSERT INTO Reviews (apt_id, user_id, date_of_rating, comment, vote)
VALUES (1, 1, '2021-09-23', 'Great Apartment, I love it!', 1);

INSERT INTO Reviews (apt_id, user_id, date_of_rating, comment, vote)
VALUES (2, 2, '2021-09-23', 'Shit Apartment, I hate it!', -1);

INSERT INTO Reviews (apt_id, user_id, date_of_rating, comment, vote)
VALUES (3, 3, '2021-09-23', 'Really Really Really Average!!', 1);

INSERT INTO Reviews (apt_id, user_id, date_of_rating, comment, vote)
VALUES (4, 4, '2000-10-03', 'Lorem ipsum dolor sit amet, 
consectetur adipiscing elit, sed do eiusmod tempor incididunt ut 
labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud 
exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. 
Duis aute irure dolor in reprehenderit in voluptate velit esse cillum 
dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non 
proident, sunt in culpa qui officia deserunt mollit anim id est laborum.', -1);

INSERT INTO Reviews (apt_id, user_id, date_of_rating, comment, vote)
VALUES (5, 5, '2021-09-10', 'EEEEEEEEEEEEEEEEEEEEEEEEEE', 1);

INSERT INTO Reviews (apt_id, user_id, date_of_rating, comment, vote)
VALUES (6, 6, '2021-09-11', 'ok I hate it!', -1);

INSERT INTO Reviews (apt_id, user_id, date_of_rating, comment, vote)
VALUES (7, 7, '2021-09-21', 'I love you!', 1);

INSERT INTO Reviews (apt_id, user_id, date_of_rating, comment, vote)
VALUES (8, 8, '2021-09-09', 'So bad Im buying it!', -1);

INSERT INTO Reviews (apt_id, user_id, date_of_rating, comment, vote)
VALUES (9, 9, '2021-09-12', 'Its not an apartment, its a flat.', 1);

INSERT INTO Reviews (apt_id, user_id, date_of_rating, comment, vote)
VALUES (10, 1, '2021-09-13', 'Be a good person', -1);

INSERT INTO Reviews (apt_id, user_id, date_of_rating, comment, vote)
VALUES (11, 2, '2021-09-14', 'Hello there lizard', 1);

INSERT INTO Reviews (apt_id, user_id, date_of_rating, comment, vote)
VALUES (12, 3, '2021-09-15', 'Windows are broken, rent is expensive, door doesnt work. Roof falling in. Bank foreclosing it. ABORT', -1);
*/