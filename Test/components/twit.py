from components.component import Component


class Twit(Component):
    def repost(self):
        self._click_button('test_repost')

    def like(self):
        self._click_button('test_like')

    def get_text(self) -> str:
        return self._get_text('test_text')

    def get_name_author(self) -> str:
        return self._get_text('test_nick_name_twit')

    def get_id_author(self) -> str:
        return self._get_text('test_id_name_twit')

    def get_count_likes(self) -> int:
        return int(self._get_text('test_like_count'))

    def get_count_reposts(self) -> int:
        return int(self._get_text('test_repost_count'))