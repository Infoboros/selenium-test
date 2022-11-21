from time import sleep

from pages import HomePage, RegisterPage, FeedPage, LoginPage
from pages.page_with_menu import PageWithMenu
from tests.fixtures import test_registration_data, test_login_data, home_page, generate_random_string


def __register(registration_page: RegisterPage, test_registration_data) -> FeedPage:
    registration_page.input_user_name(test_registration_data['username'])
    registration_page.input_user_id(test_registration_data['user_id'])

    registration_page.input_email(test_registration_data['email'])
    registration_page.input_password(test_registration_data['password'])

    return registration_page.register()


def test_case_registration(test_registration_data):
    registration_page = HomePage().transfer_registration()
    feed = __register(registration_page, test_registration_data)
    profile = PageWithMenu(feed.driver).transfer_to_profile()

    registered_nick_name = profile.get_nick_name()
    registered_id_name = profile.get_id_name()

    assert registered_nick_name == test_registration_data['username'], 'Имя не соответствует указанному при регистрации'
    assert registered_id_name == f"@{test_registration_data['user_id']}", 'Идентификатор не соответствует указанному при регистрации'

    try:
        registration_page = HomePage().transfer_registration()
        __register(registration_page, test_registration_data)
    except RegisterPage.RegistrationException as e:
        return

    assert False, 'Были зарегистрированы пользователи с одинаковыми входными данными'


def __login(login_page: LoginPage, login_data) -> FeedPage:
    login_page.input_user_name(login_data['username'])
    login_page.input_password(login_data['password'])

    return login_page.login()


def test_case_twit(home_page, test_login_data, test_registration_data):
    test_twit_text = generate_random_string(55)
    registration_page = home_page.transfer_registration()
    feed_page = __register(registration_page, test_registration_data)

    feed_page.send_twit(test_twit_text)
    last_twit_in_feed = feed_page.get_feed()[0]
    last_twit_in_feed.repost()
    last_twit_in_feed.like()

    profile_page = PageWithMenu(feed_page.driver).transfer_to_profile()
    last_twit_in_profile = profile_page.get_feed()[0]

    assert last_twit_in_profile.get_text() == test_twit_text, 'Неверный текст твита'
    assert last_twit_in_profile.get_count_likes(), 'Не установился лайк'
    assert last_twit_in_profile.get_count_reposts(), 'Не установился репост'

    notification_page = PageWithMenu(profile_page.driver).transfer_to_notification()
    notifications = notification_page.get_notifications()
    assert len(notifications) == 2, 'Пришли не все уведомления'

    login_page = HomePage().transfer_login()
    feed_page_for_other_user = __login(login_page, test_login_data)
    last_twit_for_other_user = feed_page_for_other_user.get_feed()[0]

    assert last_twit_for_other_user.get_name_author() == test_registration_data['username'], 'Имя не соответствует автору'
    assert last_twit_for_other_user.get_id_author() == f"@{test_registration_data['user_id']}", 'Идентификатор не соответствует автору'
    assert last_twit_for_other_user.get_text() == test_twit_text, 'Текст не соответствует последнему сделанному твиту'
    sleep(10)
