from selenium.webdriver.common.by import By

from components.twit import Twit
from pages.page import Page


class PageWithFeed(Page):

    def get_feed(self) -> [Twit]:
        feed = self.driver.find_element(by=By.CLASS_NAME, value='listTwits')
        twits = feed.find_elements(by=By.CLASS_NAME, value='twit')
        return [
            Twit(twit)
            for twit in twits
        ]
