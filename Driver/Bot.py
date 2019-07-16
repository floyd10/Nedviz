from .Driver import Driver
from queue import Queue
import time
from selenium.common.exceptions import *


class Bot(Driver):

    def __init__(self):
        self.links = Queue()
        super().__init__()

    def start(self):
        if not self.base_url:
            raise AttributeError("Нужно указать базовый урл")
        self.browser.get(self.base_url)
        self.browser.maximize_window()

    def end(self):
        if not self.browser:
            pass
        self.browser.quit()
        print('закрыли браузер')

    def find_links(self):
        while True:
            links_list = []
            links = self.browser.find_elements_by_xpath(
                '//div[contains(@class,"main-container")]//a[contains(@href,"sale/flat")]')
            for link in links:
                link = link.get_attribute('href')
                if link not in links_list:
                    links_list.append(link)
            print(links_list)
            for x in links_list:
                self.links.put(x)
            try:
                next_page = self.browser.find_element_by_xpath(
                '//li[contains(@class, "list-item--active")]/following::li[1]')
            except NoSuchElementException:
                break
            next_page.click()
            time.sleep(2)



    def open_links(self):
        while not self.links.empty():
            link = self.links.get()
            self.browser.get(link)


    def find_attrs(self):
        while not self.links.empty():
            link = self.links.get()
