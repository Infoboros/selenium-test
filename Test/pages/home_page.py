from pages.page import Page
from pages.login_page import LoginPage
from pages.register_page import RegisterPage


class HomePage(Page):
    def __init__(self, driver=None):
        super().__init__(driver)
        self.get('')

    def transfer_login(self) -> LoginPage:
        self.button_click('test_login')
        return LoginPage(self.driver)

    def transfer_registration(self) -> RegisterPage:
        self.button_click('test_registration')
        return RegisterPage(self.driver)

