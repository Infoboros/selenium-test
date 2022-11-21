from time import sleep

from pages import HomePage, RegisterPage, FeedPage
from pages.page_with_menu import PageWithMenu
from tests.fixtures import test_registration_data


def __register(registration_page: RegisterPage, test_registration_data) -> FeedPage:
    registration_page.input_user_name(test_registration_data['username'])
    registration_page.input_user_id(test_registration_data['user_id'])

    registration_page.input_email(test_registration_data['email'])
    registration_page.input_password(test_registration_data['password'])

    return registration_page.register()


def test_case_one(test_registration_data):
    registration_page = HomePage().transfer_registration()
    feed = __register(registration_page, test_registration_data)
    profile = PageWithMenu(feed.driver).transfer_to_profile()

    registered_nick_name = profile.get_nick_name()
    registered_id_name = profile.get_id_name()

    assert registered_nick_name == test_registration_data['username']
    assert registered_id_name == f"@{test_registration_data['user_id']}"

    sleep(10)
    try:
        registration_page = HomePage().transfer_registration()
        __register(registration_page, test_registration_data)
    except RegisterPage.RegistrationException as e:
        return

    assert False, 'Были зарегистрированы пользователи с одинаковыми входными данными'
