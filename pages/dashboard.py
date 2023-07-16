from pages.base_page import BasePage
import time

class Dashboard(BasePage):
    main_page_xpath= "//*[text()='Main page']"
    players_xpath= "//*[text()='Players']"
    polski_xpath = "//*[text()='Polski']"
    sign_out_xpath = "//*[text()='Sign out']"
    add_player_xpath = "//*[text()='Add player']"
    dev_team_contact_xpath = "//*[text()='Dev team contact']"
    scouts_panel_title_xpath = "//*[text()='Scouts panel']"
    player_count_xpath= "//*[text()='Players count']"
    matches_count_xpath = "//*[text()='Matches count']"
    reports_count_xpath = "//*[text()='Reports count']"
    events_count_xpath = "//*[text()='Events count']"
    shortcuts_count_xpath = "//*[text()='Shortcuts count']"
    activity_xpath = "//*[text()='Activity']"

    expected_title = "Scouts panel"
    dashboard_url = "https://scouts-test.futbolkolektyw.pl/en"

    add_player_url = 'https://scouts-test.futbolkolektyw.pl/en/players/add'
    add_player_expected_title= "Add player"

    def title_of_page(self):
        time.sleep(5)
        assert self.get_page_title(self.dashboard_url) == self.expected_title

    def add_player_button(self):
        self.click_on_the_element(self.add_player_xpath)
        time.sleep(5)
        assert self.get_page_title(self.add_player_url) == self.add_player_expected_title

    #pass
