from pages.base_page import BasePage


class AddMatch(BasePage):
    match_button_xpath = "//*[text()='Matches']"
    add_match_xpath = "//*[@id='__next']/div[1]/main/a/button/span[1]"
    my_team_xpath = "//*[@name='myTeam']"
    enemy_team_xpath = "//*[@name='enemyTeam']"
    my_team_score_xpath = "//*[@name='myTeamScore']"
    enemy_team_score_xpath = "//*[@name='enemyTeamScore']"
    date_xpath = "//*[@name='date']"
    match_at_home_xpath = "//*[text()='Match at home']"
    match_out_home_xpath = "//*[text()='Match out home']"
    tshirt_colour_xpath = "//*[@name='tshirt']"
    league_xpath = "//*[@name='league']"
    web_match_xpath = "//*[@name='webMatch']"
    general_xpath = "//*[@name='general']"
    rating_xpath = "//*[@name='rating']"
    submit_button_xpath = "//*[text()='Submit']"
    clear_button_xpath = "//*[text()='Clear']"
    main_page_xpath = "//*[@id='__next']/div[1]/div/div/div/ul[1]/div[1]/div[1]"
    sign_out_xpath = "//*[@id='__next']/div[1]/div/div/div/ul[3]/div[2]"
    players_xpath = "//*[@id='__next']/div[1]/div/div/div/ul[3]/div[2]"
    reports_xpath = "//*[@id='__next']/div[1]/div/div/div/ul[1]/div[2]"

    def matches(self):
        self.click_on_the_element(self.match_button_xpath)

    def add_match(self):
        self.click_on_the_element(self.add_match_xpath)
    # pass

    def type_in_my_team(self,my_team):
        self.field_send_keys(self.my_team_xpath, my_team)

    def type_in_enemy_team(self,enemy_team):
        self.field_send_keys(self.enemy_team_xpath, enemy_team)

    def type_in_my_team_score(self,my_team_score):
        self.field_send_keys(self.my_team_score_xpath,my_team_score)

    def type_in_enemy_team_score(self, enemy_team_score):
        self.field_send_keys(self.enemy_team_score_xpath, enemy_team_score)

    def type_in_date(self, date):
        self.field_send_keys(self.date_xpath, date)

    def submit(self):
        self.click_on_the_element(self.submit_button_xpath)