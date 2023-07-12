from pages.base_page import BasePage


class AddPlayer(BasePage):
    add_player_button_xpath= "//*[text()='Add player']"
    email_xpath = "//*[text()='E-mail']"
    name_xpath = "//*[@name='name']"
    surname_xpath = "//*[@name='surname']"
    phone_xpath= "//*[@name='phone']"
    submit_button_xpath= "//*[text()='Submit']"

    #def add_a_player_button(self):
        #self.click_on_the_element(self.add_player_button_xpath)
#pass