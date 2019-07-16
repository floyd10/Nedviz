from .Driver import Driver
from queue import Queue


class Bot(Driver):

    def __init__(self):
        self.links = Queue()

    def start(self):
        if not self.base_url:
            raise AttributeError("Нужно указать базовый урл")
        self.browser.get(self.base_url)
        print(dir(self))

    def find_links(self):

        self.links.put(90)
        pass

    def find_attrs(self):
        while not self.links.empty():
            link = self.links.get()
            try:
