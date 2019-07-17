from .Driver import Driver
from queue import Queue
import time
from selenium.common.exceptions import *


class Bot(Driver):

    def __init__(self):
        self.links = Queue()

    def start(self, *args):
        super().__init__()
        if self.browser is None:
            Driver.__init__()
        if not args:
            url = self.base_url
        else:
            url = args[0]
        self.browser.get(url)
        self.browser.maximize_window()

    def end(self):
        if not self.browser:
            pass
        self.browser.close()
        self.browser = None
        print('закрыли браузер')

    def find_links(self):
        links_list = []
        while True:
            links = self.browser.find_elements_by_xpath(
                '//div[contains(@class,"main-container")]//a[contains(@href,"sale/flat")]')
            for link in links:
                link = link.get_attribute('href')
                if link not in links_list:
                    links_list.append(link)
            try:
                next_page = self.browser.find_element_by_xpath(
                    '//li[contains(@class, "list-item--active")]/following::li[1]')
                next_page.click()
            except NoSuchElementException:
                break
            time.sleep(2)
        return links_list

    def open_links(self, link):
        self.start(link)
        self.browser.maximize_window()
        time.sleep(1)
        self.browser.close()

    def find_attrs(self):
        while not self.links.empty():
            link = self.links.get()
