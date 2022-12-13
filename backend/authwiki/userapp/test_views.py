import pytest
from django import urls
from django.conf import settings
from django.contrib import auth


class PytestError(Exception):
    pass


def is_logged_in(client):
    user = auth.get_user(client)
    test1 = user.is_authenticated
    private_area_url = urls.reverse('user:user_edit')
    response = client.get(private_area_url)
    test2 = response.status_code == 200
    test3 = response.wsgi_request.user.is_authenticated
    return test1 and test2 and test3


def is_not_logged_in(client):
    user = auth.get_user(client)
    test1 = not user.is_authenticated
    private_area_url = urls.reverse('user:user_edit')
    response = client.get(private_area_url)
    test2 = response.status_code == 403
    test3 = not response.wsgi_request.user.is_authenticated
    return test1 and test2 and test3


# Many tests use the authenticated_user fixture and it must be True that the
# User is logged in.
def test_authenticated_user_is_logged_in(client, authenticated_user):
    assert is_logged_in(client)


# Many tests use the created_account fixture and it must be True that the
# User is NOT logged in.
def test_created_user_is_not_logged_in(client, created_user):
    assert is_not_logged_in(client)


@pytest.mark.django_db
def test_sign_up_with_valid_data(
        client, valid_sign_up_data, django_user_model, sign_up_url):
    assert django_user_model.objects.count() == 0
    r = client.post(sign_up_url, valid_sign_up_data)
    assert r.status_code in (200, 302,)
    assert django_user_model.objects.count() == 1
    assert is_logged_in(client)


@pytest.mark.django_db
def test_login_with_valid_data(
        client, valid_login_data, django_user_model, login_url, created_user):
    assert django_user_model.objects.count() == 1
    r = client.post(login_url, valid_login_data)
    assert r.status_code in (200, 302,)
    assert is_logged_in(client)


@pytest.mark.django_db
def test_sign_up_when_passwords_dont_match(
        client, invalid_password_sign_up_data, django_user_model, sign_up_url):
    assert (
        invalid_password_sign_up_data['password1'] == 'wrong' or
        invalid_password_sign_up_data['password2'] == 'wrong')
    r = client.post(sign_up_url, invalid_password_sign_up_data)
    assert r.status_code == 200
    assert django_user_model.objects.count() == 0
    assert is_not_logged_in(client)


@pytest.mark.django_db
def test_sign_up_when_user_did_not_agree_to_terms_of_service(
        client, did_not_agree_to_tos_sign_up_data, django_user_model,
        sign_up_url):
    assert did_not_agree_to_tos_sign_up_data['agreed_to_tos'] is False
    client.post(sign_up_url, did_not_agree_to_tos_sign_up_data)
    assert is_not_logged_in(client)
    assert django_user_model.objects.count() == 0


def test_login_with_wrong_email(
        client, invalid_email_login_data, created_user, login_url):
    assert invalid_email_login_data['username'] == 'wrong@wrong.com'
    with pytest.raises(PytestError):
        client.post(login_url, data=invalid_email_login_data)
    assert is_not_logged_in(client)


def test_login_with_wrong_password(
        client, invalid_password_login_data, created_user,
        login_url):
    assert invalid_password_login_data['password'] == 'wrong'
    with pytest.raises(PytestError):
        client.post(login_url, data=invalid_password_login_data)
    assert is_not_logged_in(client)


@pytest.mark.django_db
def test_logout(client, logout_url, authenticated_user):
    r = client.get(logout_url)
    assert r.status_code == 302
    assert is_not_logged_in(client)
