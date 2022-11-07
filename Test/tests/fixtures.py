import pytest

from pages import HomePage


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
        'username': 'trname',
        'password': 'tr',
        'user_id': 'trid',
        'email': 'tr@tr.tr'
    }
