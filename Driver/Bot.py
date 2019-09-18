from .Driver import Driver
from queue import Queue
import time
from selenium.common.exceptions import *
import asyncio




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

    def start2(self, *args):
        if not args:
            url = self.base_url
        else:
            url = args[0]
        self.browser2.get(url)
        self.browser2.maximize_window()
        return self.browser2

    def end(self):
        self.browser.close()
        print('закрыли браузер')

    def returner(self, counter=-1):

        loop = asyncio.get_event_loop()
        tasks = [
            asyncio.ensure_future(self.find_links()),
            asyncio.ensure_future(self.open_links())

        ]
        loop.run_until_complete(asyncio.wait(tasks))
        loop.close()

    async def find_links(self):
        self.start()
        links_list = []
        while True:
            try:
                time.sleep(3)
                links = self.browser.find_elements_by_xpath(
                    '//div[contains(@class,"main-container")]//a[contains(@href,"sale/flat")]')
            except NoSuchElementException as e:
                print(e)
                break
            for link in links:
                link = link.get_attribute('href')
                print(f'Эту ссылку нашли на страницу{link}')
                if link not in links_list:
                    links_list.append(link)
                    self.links.put(link)
                    await self.open_links()
            try:
                next_page = self.browser.find_element_by_xpath('//li[contains(@class, "list-item--active")]/following::li[1]/a')
                print(next_page.get_attribute('InnerText'))
                next_page.click()
            except Exception as e:
                print(e)
                break

    async def open_links(self):
        while self.links.qsize()>0:
            link = self.links.get_nowait()
            print('start!')
            self.start2(link)
            #self.browser.maximize_window()
            time.sleep(1)
        



    def find_attrs(self,):
        next_page = self.browser.find_element_by_xpath(
            '//li[contains(@class, "list-item--active")]/following::li[1]')
        pass



