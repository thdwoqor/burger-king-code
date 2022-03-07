import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager


# https://synkc.tistory.com/entry/Chromedriver-DevToolsActivePort-file-doesnt-exist-%EC%97%90%EB%9F%AC-%ED%95%B4%EA%B2%B0%EB%B2%95
class BurgerKing:
    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_argument("headless")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("window-size=1920x1080")
        options.add_argument("--start-maximized")
        options.add_experimental_option("excludeSwitches", ["enable-logging"])
        options.page_load_strategy = "none"

        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), chrome_options=options)

    def run(self, *args):
        self.driver.implicitly_wait(10)
        self.driver.get(f"https://kor.tellburgerking.com/?AspxAutoDetectCookieSupport=1")
        WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="NextButton"]')))
        self.driver.find_element(By.XPATH, '//*[@id="NextButton"]').click()

        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="NextButton"]')))
        for i, value in enumerate(args):
            self.driver.find_element(By.XPATH, f'//*[@id="CN{str(i+1)}"]').send_keys(value)

        self.driver.find_element(By.XPATH, '//*[@id="NextButton"]').click()

        while True:
            try:
                WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="NextButton"]')))
                self.driver.find_element(By.XPATH, '//*[@id="NextButton"]').click()
                self.driver.find_element(By.XPATH, '//*[@id="NextButton"]').click()
            except:
                WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "ValCode")))
                return self.driver.find_element(By.CLASS_NAME, "ValCode").text
