from time import sleep

import pytest
from tests.fixtures import home_page, test_registration_data


def test_registration(home_page, test_registration_data):
    registration_page = home_page.transfer_registration()

    registration_page.input_user_name(test_registration_data['username'])
    registration_page.input_user_id(test_registration_data['user_id'])

    registration_page.input_email(test_registration_data['email'])
    registration_page.input_password(test_registration_data['password'])

    registration_page.register()
    sleep(500)

