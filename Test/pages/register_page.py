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
        # TODO эксепшн если не зарегался
        return FeedPage(self.driver)