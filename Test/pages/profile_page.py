from pages.page_with_feed import PageWithFeed


class ProfilePage(PageWithFeed):

    def get_nick_name(self) -> str:
        return self.get_text('test_nick_name')

    def get_id_name(self) -> str:
        return self.get_text('test_id_name')
