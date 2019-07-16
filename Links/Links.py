import requests
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as Ex
import re
import time

class Links:

    def __init__(self, browser):
        self.browser = browser

    @staticmethod
    def get_all_links(browser):
        # wait = WebDriverWait(self.browser, 5,poll_frequency=0.1).until(Ex.visibility_of_any_elements_located
        #                                                               (By.XPATH, ''))
        time.sleep(3)
        announce = browser.find_element_by_xpath('//*[contains(@class,"count")and contains(.,"Найдено")]/strong'). \
            get_attribute('innerText')
        nums = int(re.sub("\D", "", announce))
        print(nums)
        pages = (nums // len(browser.find_elements_by_xpath('//div[contains(@class, "offer-container")]')))
        print(pages)
        # pages = browser.find_elements_by_xpath('//a[contains(@href,"sale/flat") and text() ="Подробнее"]')
        # return pages
