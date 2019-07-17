from .Driver import Driver
from queue import Queue
import time
from selenium.common.exceptions import *
from selenium import webdriver
import os
from selenium.common import exceptions



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
        return self.browser

    def end(self):
        self.browser.close()

        print('закрыли браузер')

    def find_links(self):
        self.start()
        links_list = []
        while True:
            try:
                links = self.browser.find_elements_by_xpath(
                    '//div[contains(@class,"main-container")]//a[contains(@href,"sale/flat")]')
            except NoSuchElementException as e:
                print(e)
                break
            for link in links:
                link = link.get_attribute('href')
                if link not in links_list:
                    links_list.append(link)
                    self.links.put(link)
            try:
                next_page = self.browser.find_element_by_xpath('//li[contains(@class, "list-item--active")]/following::li[1]')
                next_page.click()
            except Exception as e:
                print(e)
                break

        return True

    def open_links(self):
        print('start!')
        while not self.links.empty():
            try:
                link = self.links.get()
                self.start(link)
                self.browser.maximize_window()
            except Exception as e:
                print(e)
                self.browser.close()

    def find_attrs(self,):
        next_page = self.browser.find_element_by_xpath(
            '//li[contains(@class, "list-item--active")]/following::li[1]')
        pass

    def returner(self, counter=-1):
        print(counter)
        try:
            if counter == -1:
                counter = 10
            while counter > 0:
                counter -= 1
                time.sleep(1)
                return self.links, self.returner(counter)
        except Exception as e:
            print(e)
            pass

