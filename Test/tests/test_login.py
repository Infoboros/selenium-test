from time import sleep

import pytest
from tests.fixtures import home_page, test_login_data


def test_login(home_page, test_login_data):
    login_page = home_page.transfer_login()

    login_page.input_user_name(test_login_data['username'])
    login_page.input_password(test_login_data['password'])

    login_page.login()
