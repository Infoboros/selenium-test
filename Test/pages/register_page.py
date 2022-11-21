from time import sleep

from pages.page import Page
from pages.feed_page import FeedPage


class RegisterPage(Page):

    def input_user_name(self, user_name: str):
        self.input_send_keys('test_username', user_name)

    def input_user_id(self, user_id: str):
        self.input_send_keys('test_user_id', user_id)

    def input_email(self, email: str):
        self.input_send_keys('test_email', email)

    def input_password(self, password: str):
        self.input_send_keys('test_password', password)

    def register(self):
        self.button_click('test_register')

        sleep(2)
        if self._get_path_from_relative('registration') == self.driver.current_url:
            raise self.RegistrationException()

        return FeedPage(self.driver)

    class RegistrationException(Page.PageException):
        def __init__(self):
            super().__init__('Ошибка во время регистрации')