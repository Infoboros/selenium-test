import random
import string

import pytest

from pages import HomePage


def generate_random_string(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for _ in range(length))


@pytest.fixture()
def home_page():
    return HomePage()


@pytest.fixture()
def test_login_data():
    return {
        'username': 't@t.t',
        'password': 't'
    }


@pytest.fixture()
def test_registration_data():
    return {
        'username': generate_random_string(5),
        'password': generate_random_string(5),
        'user_id': generate_random_string(5),
        'email': f'{generate_random_string(5)}@{generate_random_string(2)}.{generate_random_string(2)}'
    }
