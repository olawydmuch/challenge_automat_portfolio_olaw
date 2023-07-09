from pages.base_page import BasePage

class Dashboard(BasePage):
    my_team_xpath= "//*[@name='myTeam']"
    enemy_xpath= "//*[@name='enemyTeam']"
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

    pass
