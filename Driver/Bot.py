from .Driver import Driver
from queue import Queue
import time
from selenium.common.exceptions import *
from selenium import webdriver
import os


class Bot(Driver):

    def __init__(self):
        super().__init__()
        self.links = Queue()

    def start(self, *args):
        if not args:
            url = self.base_url
        else:
            url = args[0]
        self.browser.get(url)
        self.browser.maximize_window()

    def end(self):
        self.browser.close()

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

        for link in links_list[:10]:
            self.links.put(link)
        return self.links

    def open_links(self, link):
        print('start!')
        try:
            self.start(link)
            self.browser.maximize_window()
        except Exception as e:
            print(e)
            self.browser.close()

    def find_attrs(self,):
        next_page = self.browser.find_element_by_xpath(
            '//li[contains(@class, "list-item--active")]/following::li[1]')
        pass
