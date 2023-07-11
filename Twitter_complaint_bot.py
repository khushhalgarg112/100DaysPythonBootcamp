from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

chrome_driver_path = "C:\development\chromedriver.exe"

class InternetSpeedTwitterBot:

    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=chrome_driver_path)
        self.up = ""
        self.down = ""

    def get_internet_speed(self):
        self.X_PATH = '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a'
        self.driver.get("https://www.speedtest.net/")
        self.go = self.driver.find_element(By.XPATH, self.X_PATH)
        self.go.click()

        time.sleep(50)

        self.download = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span')
        self.down  = self.download.text
        print(self.down)

        self.upload = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span')
        self.up = self.upload.text
        print(self.up)


    def tweet_at_provider(self):
        self.MAIL = "gggg2002@gmail.com"
        self.driver.get(url='https://twitter.com/i/flow/login')
        time.sleep(15)
        self.id = self.driver.find_element(By.NAME, 'text')
        self.id.send_keys(self.MAIL)
        self.id.send_keys(Keys.ENTER)

        time.sleep(10)
        self.password = self.driver.find_element(By.NAME, 'password')
        self.password.send_keys("pass")
        self.password.send_keys(Keys.ENTER)

        time.sleep(10)
        self.tweet = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/header/div/div/div/div[1]/div[3]/a')
        self.tweet.click()
        time.sleep(10)                              

        self.content = self.driver.find_element(By.CSS_SELECTOR, '.DraftEditor-root div div div div div span')
        self.content.send_keys(f"Hello @JioCare my speed is {self.down}Mb/s even my 5G is activated. ")

        time.sleep(10)
        self.sent = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div[2]/div[1]/div/div/div/div[2]/div[2]/div/div/div[2]/div[4]')
        self.sent.click()                               

complain = InternetSpeedTwitterBot()

complain.get_internet_speed()
time.sleep(5)
complain.tweet_at_provider()

'''ComplainetBot'''