"""This is a scraper to scrape uiucApts.htm file"""
import re
import sqlite3
from bs4 import BeautifulSoup
from dataclasses import dataclass

con = sqlite3.connect("database_prod.db")


@dataclass
class AptInfo:
    """Apt class, stores detail about an apartment"""

    name: str
    url: str
    addr: str
    price_range: str


def scraper():
    """I am a scraper"""
    with open("uiucApts.htm", "r", encoding="UTF-8") as file:
        soup = BeautifulSoup(file.read(), features="html.parser")
        apts = soup.find_all("div", class_="c-list")
        for i, apt in enumerate(apts):
            mobile_header = apt.find("div", class_="mobileHeader")
            image_section = apt.find("div", class_="slick-track")
            campus_detail = apt.find("div", class_="campusDetail")
            apt = read_apt(mobile_header, campus_detail)

            apt_price_min, apt_price_max = format_price(apt.price_range)

            write_to_apt_db(
                i, [apt.name, apt.addr, apt_price_min, apt_price_max, apt.url]
            )
            if image_section:
                imgs = image_section.findAll("img")
                for idx, img in enumerate(imgs):
                    if idx == 0:
                        write_to_img_db(i, img["src"])
                    if idx > 0:
                        write_to_img_db(i, img["data-lazy"])
        con.commit()


def read_apt(header, detail):
    """ A helper function to read apt in to apt dataclass"""
    apt_name = header.find("a").text
    apt_url = header.find("a")["href"]
    apt_addr = header.find("span", class_="ellipsis").text
    price_range = detail.find("em", class_="rent_style").text.strip()
    return AptInfo(apt_name, apt_url, apt_addr, price_range)


def format_price(price_range):
    """A helper function to format string"""
    if re.search("[a-aA-Z]", price_range):
        return -1, -1  # price not avaiable
    res = re.findall(r"\d+", price_range)
    if len(res) == 1:
        return [int(res[0]), int(res[0])]  # only has one price
    if len(res) == 4:  # decimal price
        return [int(res[0]), int(res[2])]
    return [int(res[0]), int(res[1])]


def write_to_apt_db(apt_id, info):
    """A helper function to execute INSERT into Apartments"""
    cur = con.cursor()
    cur.execute(
        "INSERT INTO Apartments (apt_id, apt_name, apt_address, price_min, price_max, link) \
        VALUES (?, ?, ?, ?, ?, ?)",
        (apt_id, info[0], info[1], info[2], info[3], info[4]),
    )


def write_to_img_db(apt_id, url):
    """A helper function to execute INSERT into AptPics"""
    cur = con.cursor()
    cur.execute(
        "INSERT INTO AptPics (apt_id, link) \
        VALUES (?, ?)",
        (apt_id, url),
    )


scraper()
print("Import to DB successfully.")
