"""This is a scraper to scrape uiucApts.htm file"""
import re
import sqlite3
from bs4 import BeautifulSoup

con = sqlite3.connect("database_prod.db")

"""I am a scraper"""


def scraper():
    with open("uiucApts.htm", "r", encoding="UTF-8") as file:
        content = file.read()
        soup = BeautifulSoup(content, features="html.parser")
        apts = soup.find_all("div", class_="c-list")
        for i, apt in enumerate(apts):
            mobile_header = apt.find("div", class_="mobileHeader")
            image_section = apt.find("div", class_="slick-track")
            campus_detail = apt.find("div", class_="campusDetail")

            apt_name = mobile_header.find("a").text
            apt_url = mobile_header.find("a")["href"]
            apt_addr = mobile_header.find("span", class_="ellipsis").text
            price_range = campus_detail.find("em", class_="rent_style").text.strip()
            apt_price_min, apt_price_max = format_price(price_range)

            write_to_apt_db(
                i, apt_name, apt_addr, apt_price_min, apt_price_max, apt_url
            )
            if image_section:
                imgs = image_section.findAll("img")
                for idx, img in enumerate(imgs):
                    if idx == 0:
                        write_to_img_db(i, img["src"])
                    if idx > 0:
                        write_to_img_db(i, img["data-lazy"])
        con.commit()


"""A helper function to format string"""


def format_price(price_range):
    if re.search("[a-aA-Z]", price_range):
        return -1, -1  # price not avaiable
    res = re.findall(r"\d+", price_range)
    if len(res) == 1:
        return [int(res[0]), int(res[0])]  # only has one price
    if len(res) == 4:  # decimal price
        return [int(res[0]), int(res[2])]
    return [int(res[0]), int(res[1])]


"""A helper function to execute INSERT into Apartments"""


def write_to_apt_db(id, name, addr, pmin, pmax, url):
    cur = con.cursor()
    cur.execute(
        "INSERT INTO Apartments (apt_id, apt_name, apt_address, price_min, price_max, link) \
        VALUES (?, ?, ?, ?, ?, ?)",
        (id, name, addr, pmin, pmax, url),
    )


"""A helper function to execute INSERT into AptPics"""


def write_to_img_db(id, url):
    cur = con.cursor()
    cur.execute(
        "INSERT INTO AptPics (apt_id, link) \
        VALUES (?, ?)",
        (id, url),
    )


scraper()
print("Import to DB successfully.")
