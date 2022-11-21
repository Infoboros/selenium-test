from time import sleep

from pages.page_with_feed import PageWithFeed


class FeedPage(PageWithFeed):
    def send_twit(self, text: str):
        self.input_send_keys('test_text_twit_field', text)
        self.button_click('test_make_twit_button')
        sleep(2)
