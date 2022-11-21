from selenium.webdriver.remote.webelement import WebElement


class Component:
    def __init__(self, element: WebElement):
        self.element = element

    def _click_button(self, button_id: str):
        button = self.element.find_element(value=button_id)
        button.click()

    def _get_text(self, block_id: str):
        block = self.element.find_element(value=block_id)
        return block.text
