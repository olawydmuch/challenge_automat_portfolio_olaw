from pages.base_page import BasePage

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

    pass
