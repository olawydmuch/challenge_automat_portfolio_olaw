from pages.base_page import BasePage


class AddPlayer(BasePage):
    add_player_button_xpath= "//*[text()='Add player']"
    email_xpath = "//*[text()='E-mail']"
    name_xpath = "//*[@name='name']"
    surname_xpath = "//*[@name='surname']"
    phone_xpath= "//*[@name='phone']"
    submit_button_xpath= "//*[text()='Submit']"

    add_player_url = 'https://scouts-test.futbolkolektyw.pl/en/players/add'
    add_player_expected_title = "Add player"

    def title_of_add_player_page(self):
        assert self.get_page_title(self.add_player_url) == self.add_player_expected_title
#pass