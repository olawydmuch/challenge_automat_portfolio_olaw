from pages.base_page import BasePage


class ChangeLanguage(BasePage):
    login_field_xpath = "//*[@id='login']"
    password_field_xpath = "//*[@id='password']"
    sign_in_button_xpath = "//*[text()='Sign in']"
    login_url = ('https://scouts-test.futbolkolektyw.pl/en')
    expected_title = 'Scouts panel - sign in'
    sign_out_button_xpath = "//*[text()='Sign out']"
    expected_text = 'Scouts Panel'
    polski_xpath= "//*[text()='Polski']"

    def type_in_email(self, email):
        self.field_send_keys(self.login_field_xpath, email)

    def enter_password(self, password):
        self.field_send_keys(self.password_field_xpath, password)

    def sign_in(self):
        self.click_on_the_element(self.sign_in_button_xpath)

    def polski_language(self):
        self.click_on_the_element(self.polski_xpath)

    def title_of_page(self):
        assert self.get_page_title(self.login_url) == self.expected_title

    def change_language_to_polish(self):
        polish_page_xpath = "//*[text()='Strona główna']"
        self.assertEqual(polish_page_xpath, u"Strona główna")


