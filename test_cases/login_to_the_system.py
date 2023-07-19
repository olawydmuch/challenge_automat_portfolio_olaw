import os
import time
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from pages.login_page import LoginPage
from pages.base_page import BasePage
from pages.dashboard import Dashboard

from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT

class TestLoginPage(unittest.TestCase):

    @classmethod
    def setUp(self):
        os.chmod(DRIVER_PATH, 755)
        self.driver_service = Service(executable_path=DRIVER_PATH)
        self.driver = webdriver.Chrome(service=self.driver_service)
        self.driver.get('https://scouts-test.futbolkolektyw.pl/en')
        self.driver.fullscreen_window()
        self.driver.implicitly_wait(IMPLICITLY_WAIT)

    def test_login_to_the_system(self):

        user_login = LoginPage(self.driver)
        user_login.title_of_page()
        user_login.type_in_email('user01@getnada.com')
        user_login.enter_password('Test-1234')
        user_login.sign_in()
        dashboard_page = Dashboard(self.driver)
        dashboard_page.title_of_page()
        time.sleep(10)

    # TC5 "Log out"
    def test_logout(self):
        user_login = LoginPage(self.driver)
        user_login.title_of_page()
        user_login.type_in_email('user02@getnada.com')
        user_login.enter_password('Test-1234')
        user_login.sign_in()
        time.sleep(5)
        user_login.sign_out()
        dashboard_page = Dashboard(self.driver)
        time.sleep(5)
        dashboard_page.title_of_logout_page()

    #TC2 (Login into webside with incorrect login data)

    def test_incorrect_login(self):
        user_login = LoginPage(self.driver)
        user_login.title_of_page()
        user_login.type_in_email('user01@getnada.com')
        user_login.enter_password('Test12345')
        user_login.sign_in()
        time.sleep(5)
        dashboard_page = Dashboard(self.driver)
        time.sleep(5)
        dashboard_page.announcement_of_incorrect_login()
        time.sleep(5)

    @classmethod
    def tearDown(self):
        self.driver.quit()
