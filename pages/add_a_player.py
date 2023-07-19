from pages.base_page import BasePage


class AddPlayer(BasePage):
    login_field_xpath = "//*[@id='login']"
    password_field_xpath = "//*[@id='password']"
    sign_in_button_xpath = "//*[text()='Sign in']"
    login_url = ('https://scouts-test.futbolkolektyw.pl/en')
    add_player_button_xpath= "//*[text()='Add player']"
    email_xpath = "//*[@name='email']"
    name_xpath = "//*[@name='name']"
    surname_xpath = "//*[@name='surname']"
    phone_xpath= "//*[@name='phone']"
    weight_xpath = "//*[@name='weight']"
    height_xpath = "//*[@name='height']"
    age_xpath = "//*[@name='age']"
    main_position_xpath = "//*[@name='mainPosition']"
    submit_button_xpath= "//*[text()='Submit']"

    add_player_url = 'https://scouts-test.futbolkolektyw.pl/en/players/add'
    add_player_expected_title = "Add player"

    def title_of_add_player_page(self):
        assert self.get_page_title(self.add_player_url) == self.add_player_expected_title

    def type_in_email(self,email):
        self.field_send_keys(self.email_xpath, email)

    def type_in_name(self,name):
        self.field_send_keys(self.name_xpath, name)

    def type_in_surname(self,surname):
        self.field_send_keys(self.surname_xpath, surname)

    def type_in_phone(self,phone):
        self.field_send_keys(self.phone_xpath, phone)

    def type_in_weight(self,weight):
        self.field_send_keys(self.weight_xpath, weight)

    def type_in_height(self,height):
        self.field_send_keys(self.height_xpath, height)

    def type_in_age(self,age):
        self.field_send_keys(self.age_xpath, age)

    def type_in_main_position(self,main_position):
        self.field_send_keys(self.main_position_xpath, main_position)

    def submit(self):
        self.click_on_the_element(self.submit_button_xpath)
#pass