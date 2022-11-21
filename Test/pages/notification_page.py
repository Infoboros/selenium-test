from components.notification import Notification
from pages import Page


class NotificationPage(Page):

    def get_notifications(self) -> [Notification]:
        notification_feed = self.driver.find_element(value='test_notification_feed')
        notifications = notification_feed.find_elements(value='test_notification')
        return [
            Notification(notification)
            for notification in notifications
        ]