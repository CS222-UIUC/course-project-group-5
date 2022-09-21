from email.mime import image
from lib2to3.pgen2 import driver
from time import sleep
from bs4 import BeautifulSoup

class Apt:
    def __init__(self, name, addr):
        self.name = name
        self.addr = addr
        self.img = []
        self.contact_number = ""
    def add_imgs(img):
        img.append(img)
    def add_contact_number(number):
        contact_number = number
        
with open(r"D:\AptRating\uiucApts.htm", "r") as f:
    content = f.read()
    soup = BeautifulSoup(content, features="html.parser")
    apts = soup.find_all("div", class_="c-list")
    for i, apt in enumerate(apts):
        mobileHeader = apt.find("div", class_="mobileHeader")
        imageSection = apt.find("div", class_="imageSection")
        campusDetail = apt.find("div", class_="campusDetail")
        
        apt_name = mobileHeader.find("a").text
        apt_addr = mobileHeader.find("span", class_="ellipsis").text
        apt = Apt(apt_name, apt_addr)
        imgs = imageSection.findAll("img") 
        
        # for img in imgs:
        #     if img.has_attr("src"):
        #         apt.add_imgs(img["src"])
        #     else:
        #         apt.add_imgs(img["data-lazy"])
        
        apt_call = campusDetail.find("b").text
        apt_price = campusDetail.find("em", class_="rent_style").text.strip()
        print(apt_price)
        print("================")