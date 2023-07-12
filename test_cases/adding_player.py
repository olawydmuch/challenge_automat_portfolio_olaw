import os
import time
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from pages.login_page import LoginPage
from pages.dashboard import Dashboard
from pages.add_a_player import AddPlayer

from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT

class TestAddPlayer(unittest.TestCase):

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
        dashboard_page.add_player_page()
        time.sleep(5)

    @classmethod
    def tearDown(self):
        self.driver.quit()