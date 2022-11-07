from abc import ABC
from selenium import webdriver
from config import manager, options, base_url


class Page(ABC):
    def __init__(self, driver=None):
        self.driver = driver or webdriver.Chrome(
            manager,
            chrome_options=options
        )

    def get(self, relative: str):
        return self.driver.get(f'{base_url}/{relative}')

    def button_click(self, button_id: str):
        login_button = self.driver.find_element(value=button_id)
        login_button.click()

    def input_send_keys(self, input_id: str, keys: str):
        input_field = self.driver.find_element(value=input_id)
        input_field.send_keys(keys)
