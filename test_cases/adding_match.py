import os
import time
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from pages.add_a_match_form import AddMatch
from pages.login_page import LoginPage
from pages.dashboard import Dashboard
from pages.add_a_player import AddPlayer

from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT

class TestAddMatch(unittest.TestCase):

    @classmethod
    def setUp(self):
        os.chmod(DRIVER_PATH, 755)
        self.driver_service = Service(executable_path=DRIVER_PATH)
        self.driver = webdriver.Chrome(service=self.driver_service)
        self.driver.get('https://scouts-test.futbolkolektyw.pl/en')
        self.driver.fullscreen_window()
        self.driver.implicitly_wait(IMPLICITLY_WAIT)

#TC3 (Checking the correct operation of the form for adding a match)
    def test_adding_match(self):
        user_login = LoginPage(self.driver)
        user_login.title_of_page()
        user_login.type_in_email('user01@getnada.com')
        user_login.enter_password('Test-1234')
        user_login.sign_in()
        dashboard_page = Dashboard(self.driver)
        time.sleep(10)
        dashboard_page.add_player_button()
        time.sleep(5)

        add_player = AddPlayer(self.driver)
        time.sleep(10)
        add_player.type_in_name('Andrzej')
        add_player.type_in_surname('Andrzejewski')
        add_player.type_in_age('01.01.2000')
        add_player.type_in_main_position('keeper')
        add_player.submit()
        time.sleep(10)

        add_match = AddMatch(self.driver)
        time.sleep(5)
        add_match.matches()
        time.sleep(5)
        add_match.add_match()

        add_match.type_in_my_team('FC Janusz')
        add_match.type_in_enemy_team('FC Grazyna')
        add_match.type_in_my_team_score('1')
        add_match.type_in_enemy_team_score('0')
        add_match.type_in_date('10.10.2022')
        add_match.submit()
        time.sleep(10)

    @classmethod
    def tearDown(self):
        self.driver.quit()

