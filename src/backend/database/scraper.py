from bs4 import BeautifulSoup
import re
import sqlite3

con = sqlite3.connect("database_prod.db")


def scraper():
    with open("uiucApts.htm", "r") as f:
        content = f.read()
        soup = BeautifulSoup(content, features="html.parser")
        apts = soup.find_all("div", class_="c-list")
        for i, apt in enumerate(apts):
            mobileHeader = apt.find("div", class_="mobileHeader")
            imageSection = apt.find("div", class_="slick-track")
            campusDetail = apt.find("div", class_="campusDetail")

            apt_name = mobileHeader.find("a").text
            apt_url = mobileHeader.find("a")["href"]
            apt_addr = mobileHeader.find("span", class_="ellipsis").text
            price_range = campusDetail.find("em", class_="rent_style").text.strip()
            apt_price_min, apt_price_max = format_price(price_range)

            writeToAptDB(i, apt_name, apt_addr, apt_price_min, apt_price_max, apt_url)
            if imageSection:
                imgs = imageSection.findAll("img")
                for idx, img in enumerate(imgs):
                    if idx == 0:
                        writeToImgDB(i, img["src"])
                    if idx > 0:
                        writeToImgDB(i, img["data-lazy"])
        con.commit()


def format_price(price_range):
    if re.search("[a-aA-Z]", price_range):
        return -1, -1  # price not avaiable
    res = re.findall(r"\d+", price_range)
    if len(res) == 1:
        return [int(res[0]), int(res[0])]  # only has one price
    if len(res) == 4:  # decimal price
        return [int(res[0]), int(res[2])]
    return [int(res[0]), int(res[1])]


def writeToAptDB(id, name, addr, pmin, pmax, url):
    cur = con.cursor()
    cur.execute(
        "INSERT INTO Apartments (apt_id, apt_name, apt_address, price_min, price_max, link) \
        VALUES (?, ?, ?, ?, ?, ?)",
        (id, name, addr, pmin, pmax, url),
    )


def writeToImgDB(id, url):
    cur = con.cursor()
    cur.execute(
        "INSERT INTO AptPics (apt_id, link) \
        VALUES (?, ?)",
        (id, url),
    )


scraper()
print("Import to DB successfully.")
