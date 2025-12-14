from selenium import webdriver

from fixture.session import SessionHelper
from selenium.webdriver.support.ui import Select
from fixture.project import ProjectHelper
from fixture.james import JamesHelper


class Application:

    def __init__(self, browser, config):
        if browser == "chrome":
            self.wd = webdriver.Chrome()
        elif browser == "firefox":
            self.wd = webdriver.Firefox()
        elif browser == "ie":
            self.wd = webdriver.Ie()
        else:
            raise ValueError("Unrecognized browser %s" % browser)
        # self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(2)
        self.session = SessionHelper(self)
        self.Select = Select
        self.base_url = config['web']['baseUrl']
        self.project = ProjectHelper(self)
        self.james = JamesHelper(self)
        self.config = config

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except: # нас интересуют все проблемы
            return False

    def open_home_page(self):
        wd = self.wd
        wd.get(self.base_url)

    def destroy(self):
        self.wd.quit()