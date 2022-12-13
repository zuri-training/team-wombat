import copy
import pytest
from django import urls


@pytest.fixture(scope='session')
def valid_sign_up_data():
    return {
        'email': 't@t.com',
        'password1': 'testpassword',
        'password2': 'testpassword',
        'agreed_to_tos': True,
    }


@pytest.fixture
def created_user(django_user_model, valid_login_data):
    user = django_user_model.objects.create_user(
        email=valid_login_data['username'],
        password=valid_login_data['password'])
    user.set_password(valid_login_data['password'])
    return user


@pytest.fixture
def authenticated_user(client, created_user, valid_login_data):
    # client.force_login(created_user) doesn't work so we are using
    # client.login isntead. Is this a bug in pytest?
    client.login(
        email=valid_login_data['username'], password=valid_login_data['password'])
    return created_user


@pytest.fixture(scope='session')
def invalid_password_sign_up_data(valid_sign_up_data):
    data = copy.copy(valid_sign_up_data)
    assert 'password1' in data
    data['password1'] = 'wrong'
    return data


@pytest.fixture(scope='session')
def did_not_agree_to_tos_sign_up_data(valid_sign_up_data):
    data = copy.copy(valid_sign_up_data)
    data['agreed_to_tos'] = False
    return data


@pytest.fixture(scope='session')
def valid_login_data(valid_sign_up_data):
    pw1 = valid_sign_up_data.get('password1')
    pw2 = valid_sign_up_data.get('password2')
    assert pw1 == pw2
    email = valid_sign_up_data['email']
    return {'username': email, 'password': pw1}


@pytest.fixture(scope='session')
def invalid_email_login_data(valid_login_data):
    data = copy.copy(valid_login_data)
    data['username'] = 'wrong@wrong.com'
    return data


@pytest.fixture(scope='session')
def invalid_password_login_data(valid_login_data):
    data = copy.copy(valid_login_data)
    data['password'] = 'wrong'
    return data


@pytest.fixture(scope='session')
def login_url():
    return urls.reverse('login')


@pytest.fixture(scope='session')
def logout_url():
    return urls.reverse('logout')


@pytest.fixture(scope='session')
def sign_up_url():
    return urls.reverse('sign_up')
