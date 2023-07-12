from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.common.exceptions import ElementClickInterceptedException

chrome_path = "C:\development\chromedriver.exe"
SIMILAR_ACCOUNT  = "codes.learning"

class InstagramBot:

    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=chrome_path)

    def login(self):
        self.driver.get("https://www.instagram.com/accounts/login/")
        time.sleep(5)
        user  = self.driver.find_element(By.NAME, "username")
        user.send_keys("developers_home_")
        password = self.driver.find_element(By.NAME, "password")
        password.send_keys("Khushal123@")
        password.send_keys(Keys.ENTER)

        time.sleep(5)

        # not_now  = self.driver.find_element(By.CSS_SELECTOR, 'section main div div div div')
        # not_now.click()

    def find_followers(self):
        self.driver.get(f"https://www.instagram.com/{SIMILAR_ACCOUNT}")
        self.driver.maximize_window()
        time.sleep(5)

        self.followers = self.driver.find_element(By.CSS_SELECTOR, "section ul a")
        self.followers.click()

        time.sleep(5)
        modal = self.driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]')
        for i in range(10):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
            time.sleep(2)

        
    def follow(self):
        follow = self.driver.find_elements(By.CSS_SELECTOR, "._aano button")

        for i in follow:
            try:   
                i.click()

            except ElementClickInterceptedException:
                cancel_button = self.driver.find_element(By.CLASS_NAME, "_a9_1")
                cancel_button.click()


bot = InstagramBot()
bot.login()
bot.find_followers()
bot.follow()

