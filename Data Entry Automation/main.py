from selenium import webdriver
from bs4 import BeautifulSoup
import requests
from selenium.webdriver.common.by import By
import time


chrome_path = "C:\development\chromedriver.exe"

FORM = "https://docs.google.com/forms/d/e/1FAIpQLSer9o1rfgnW0gAWInjZag3blEgWlU3S-_a17XT1d6C1RYOYRA/viewform?usp=sf_link"
ADDRESS = []
PRICE = []
LINK = []

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8",
}


class HouseData:
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=chrome_path)

        self.web = requests.get(
            "https://www.zillow.com/homes/for_rent/1-_beds/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3Anull%2C%22mapBounds%22%3A%7B%22west%22%3A-122.56276167822266%2C%22east%22%3A-122.30389632177734%2C%22south%22%3A37.69261345230467%2C%22north%22%3A37.857877098316834%7D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22pmf%22%3A%7B%22value%22%3Afalse%7D%2C%22pf%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A12%7D",
            headers=HEADERS,
        )
        self.my_html = self.web.content

        self.soup = BeautifulSoup(self.my_html, "html.parser")

    def scrape(self):
        # print(self.soup.prettify())
        address = self.soup.find_all(class_=self.my_css)
        price = self.soup.find_all(class_=self.my_price)
        for i in address:
            ADDRESS.append(i.text)
            LINK.append(f'https://www.zillow.com{i.get("href")}')

        for j in price:
            PRICE.append(j.text)
            
    def my_css(self, css_class):
        return (
            css_class is not None
            and "StyledPropertyCardDataArea-c11n-8-89-0__sc-yipmu-0 gZUDVm property-card-link"
            in css_class
        )

    def my_price(self, css_class):
        return (
            css_class is not None
            and "PropertyCardWrapper__StyledPriceLine-srp__sc-16e8gqd-1 iMKTKr"
            in css_class
        )

    def form(self):
        for i in range(len(ADDRESS)):
            self.driver.get(FORM)
            time.sleep(1)
            ad = self.driver.find_element(
                By.XPATH,
                "/html/body/div/div[2]/form/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input",
            )
            ad.send_keys(ADDRESS[i])

            pr = self.driver.find_element(
                By.XPATH,
                "/html/body/div/div[2]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input",
            )
            pr.send_keys(PRICE[i])

            li = self.driver.find_element(
                By.XPATH,
                "/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input",
            )
            li.send_keys(LINK[i])

            submit = self.driver.find_element(
                By.XPATH,
                "/html/body/div/div[2]/form/div[2]/div/div[3]/div[1]/div[1]/div",
            )
            submit.click()


bot = HouseData()
bot.scrape()
bot.form()
