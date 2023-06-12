from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import json
from itertools import zip_longest

# Replace with the path to your chromedriver executable
CHROME_PATH = r"C:\Users\xsile\AppData\Local\Google\Chrome\Application\chrome.exe"


class Scraper:
    def __init__(self, input_data):
        """
        Args: input_data
            Options:
                "zahajeni"
                "preruseni"
                "ukonceni"
                "obnoveni"
        """
        self.input_data = input_data
        self.chrome_options = Options()
        self.chrome_options.add_argument("--headless")
        self.chrome_options.add_argument("--no-sandbox")
        self.chrome_options.add_argument("--disable-dev-shm-usage")
        self.webdriver_service = Service(CHROME_PATH)
        self.output_data = []

    def initialize_driver(self):
        self.driver = webdriver.Chrome(
            service=self.webdriver_service, options=self.chrome_options)
        self.driver.get("https://prehledy.sukl.cz/mr.html#/")
        self.wait = WebDriverWait(self.driver, 10)

    def scrape_data(self):
        button = '//*[@id="root"]/div/div/div[2]/div/div[2]/div/div/div[2]/div[1]/div/div[2]/div/div/div[1]/button'

        clickable_li_Xpath = {
            "zahajeni": '//*[@id="root"]/div/div/div[2]/div/div[2]/div/div/div[2]/div[1]/div/div[2]/div/div/div[2]/ul/li[2]',
            "preruseni": '//*[@id="root"]/div/div/div[2]/div/div[2]/div/div/div[2]/div[1]/div/div[2]/div/div/div[2]/ul/li[3]',
            "ukonceni": '//*[@id="root"]/div/div/div[2]/div/div[2]/div/div/div[2]/div[1]/div/div[2]/div/div/div[2]/ul/li[4]',
            "obnoveni": '//*[@id="root"]/div/div/div[2]/div/div[2]/div/div/div[2]/div[1]/div/div[2]/div/div/div[2]/ul/li[5]',
        }

        selected = clickable_li_Xpath.get(self.input_data)

        self.driver.find_element(By.XPATH, button).click()
        self.driver.find_element(By.XPATH, selected).click()
        time.sleep(1)
        table = self.wait.until(EC.presence_of_element_located(
            (By.CLASS_NAME, "sukl-data-table")))

        drugs = []

        rows = table.find_elements(By.CLASS_NAME, "sukl-data-table__row")

        for row in rows:

            cells = row.find_elements(By.TAG_NAME, "div")
            for cell in cells:
                drugs.append(cell.text)

        head = self.driver.find_elements(
            By.CLASS_NAME, "sukl-data-table__header-cell")
        keys = [ele.text for ele in head if ele.text != ""]

        chunk_size = 14
        new_list = []

        for i in range(0, 140, chunk_size):
            chunk = drugs[i:i+chunk_size]
            new_list.append(chunk)

        self.output_data = []
        for n in range(len(new_list)):
            data = {key: value for key,
                    value in zip_longest(keys, new_list[n])}
            data.pop(None, None)
            self.output_data.append(data)

        self.driver.quit()

    def save_json(self):
        with open("data.json", "w") as f:
            json.dump(self.output_data, f)
            print("Data saved succesfully to 'data.json' file.")
