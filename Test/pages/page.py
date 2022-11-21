from abc import ABC
from selenium import webdriver
from config import manager, options, base_url


class Page(ABC):
    def __init__(self, driver=None):
        self.driver = driver or webdriver.Chrome(
            manager,
            chrome_options=options
        )

    @staticmethod
    def _get_path_from_relative(relative_path: str) -> str:
        return f'{base_url}/{relative_path}'

    def get(self, relative: str):
        return self.driver.get(
            self._get_path_from_relative(relative)
        )

    def button_click(self, button_id: str):
        login_button = self.driver.find_element(value=button_id)
        login_button.click()

    def input_send_keys(self, input_id: str, keys: str):
        input_field = self.driver.find_element(value=input_id)
        input_field.send_keys(keys)

    def get_text(self, block_id: str):
        block = self.driver.find_element(value=block_id)
        return block.text

    class PageException(Exception):
        pass
