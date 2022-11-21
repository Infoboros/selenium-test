from time import sleep

from pages.page import Page
from pages.feed_page import FeedPage
from pages.notification_page import NotificationPage
from pages.profile_page import ProfilePage


class PageWithMenu(Page):

    def transfer_to_feed(self) -> FeedPage:
        self.button_click('feed')
        sleep(2)
        return FeedPage(self.driver)

    def transfer_to_notification(self) -> NotificationPage:
        self.button_click('notification')
        sleep(2)
        return NotificationPage(self.driver)

    def transfer_to_profile(self) -> ProfilePage:
        self.button_click('profile')
        sleep(2)
        return ProfilePage(self.driver)
