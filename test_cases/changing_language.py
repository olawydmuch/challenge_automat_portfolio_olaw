import os
import time
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from pages.change_of_the_language import ChangeLanguage

from pages.dashboard import Dashboard

from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT

class TestChangeLanguage(unittest.TestCase):

    @classmethod
    def setUp(self):
        os.chmod(DRIVER_PATH, 755)
        self.driver_service = Service(executable_path=DRIVER_PATH)
        self.driver = webdriver.Chrome(service=self.driver_service)
        self.driver.get('https://scouts-test.futbolkolektyw.pl/en')
        self.driver.fullscreen_window()
        self.driver.implicitly_wait(IMPLICITLY_WAIT)

#TC4 (Verification of the correctness of changing the language from English to Polish)
    def test_changing_language(self):
        user_login = ChangeLanguage(self.driver)
        user_login.title_of_page()
        user_login.type_in_email('user01@getnada.com')
        user_login.enter_password('Test-1234')
        user_login.sign_in()
        time.sleep(10)

        change_language = ChangeLanguage(self.driver)
        change_language.polski_language()
        time.sleep(5)
        #dashboard_page = Dashboard(self.driver)
        #dashboard_page.change_language_to_polish()

    @classmethod
    def tearDown(self):
        self.driver.quit()

