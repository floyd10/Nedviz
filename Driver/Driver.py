import os
from selenium import webdriver


class Driver:

    def __init__(self):
        self.base_dir = os.path.dirname(os.path.abspath(__package__))
        self.chromedriver = os.path.join(self.base_dir, "chromedriver.exe")
        self.options = webdriver.ChromeOptions()
        #self.options.add_argument('headless')
        self.browser = webdriver.Chrome(executable_path=self.chromedriver, options=self.options)
