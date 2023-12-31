import self as self
from pages.base_page import BasePage


class LoginPage(BasePage):
    login_field_xpath = "//*[@id='login']"
    password_field_xpath = "//*[@id='password']"
    sign_in_button_xpath = "//*[text()='Sign in']"
    login_url = ('https://scouts-test.futbolkolektyw.pl/en')
    expected_title = 'Scouts panel - sign in'
    sign_out_button_xpath = "//*[text()='Sign out']"
    expected_text= 'Scouts Panel'


    def type_in_email(self, email):
        self.field_send_keys(self.login_field_xpath, email)

    def enter_password(self, password):
        self.field_send_keys(self.password_field_xpath, password)

    def sign_in(self):
        self.click_on_the_element(self.sign_in_button_xpath)

    def title_of_page(self):
        assert self.get_page_title(self.login_url) == self.expected_title

    def sign_out(self):
            self.click_on_the_element(self.sign_out_button_xpath)

    def title_of_logout_page(self):
        assert self.get_page_title(self.login_url) == self.expected_text

    def announcement_of_incorrect_login(self):
        assert self.get_page_title(self.login_url) == self.announcement_incorrect_login