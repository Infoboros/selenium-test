from pages.page import Page
from pages.feed_page import FeedPage


class LoginPage(Page):

    def input_user_name(self, user_name: str):
        self.input_send_keys('test_username', user_name)

    def input_password(self, password: str):
        self.input_send_keys('test_password', password)

    def login(self):
        self.button_click('test_login')
        # TODO эксепшн если не вошло
        return FeedPage(self.driver)