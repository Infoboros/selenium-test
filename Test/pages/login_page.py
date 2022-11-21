from time import sleep

from pages.page import Page
from pages.feed_page import FeedPage


class LoginPage(Page):

    def input_user_name(self, user_name: str):
        self.input_send_keys('test_username', user_name)

    def input_password(self, password: str):
        self.input_send_keys('test_password', password)

    def login(self):
        self.button_click('test_login')

        sleep(2)
        if self._get_path_from_relative('login') == self.driver.current_url:
            raise self.LoginException()

        return FeedPage(self.driver)

    class LoginException(Page.PageException):
        def __init__(self):
            super().__init__('Ошибка во время аутентификации')