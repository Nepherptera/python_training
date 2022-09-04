from selenium import webdriver
from selenium.webdriver.support.select import Select

from fixture.group import GroupHelper
from fixture.session import SessionHelper
from fixture.contact import ContactHelper


class Application:  # Класс, в котором содержатся все вспомогательные методы

    def __init__(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(1)
        self.session = SessionHelper(self)  # ссылка на фикстуру, которую передаем в помощника session
        self.group = GroupHelper(self)
        self.contact = ContactHelper(self)

    def is_valid(self):
        try:
            self.wd.current_url()
            return True
        except:
            return False

    def open_home_page(self):
        wd = self.wd
        if not (wd.current_url == "http://localhost/addressbook/"):
            wd.get("http://localhost/addressbook/")

    def destroy(self):
        self.wd.quit()