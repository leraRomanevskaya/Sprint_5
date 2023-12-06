import pytest

from methods import get_random_login
from methods import get_random_password
from selenium import webdriver


@pytest.fixture  # имя
def name():
    name = 'Лера'
    return name


@pytest.fixture  # рандомный e-mail
def random_email():
    email = get_random_login()
    return email


@pytest.fixture  # e-mail
def email():
    email = 'fairkat@mail.ru'
    return email


@pytest.fixture  # рандомный корректный пароль
def random_corr_password():
    password = get_random_password()
    return password


@pytest.fixture  # корректный пароль
def corr_password():
    password = '123456'
    return password


@pytest.fixture  # некорректный пароль
def uncorr_password():
    password = '12345'
    return password


@pytest.fixture  # страница входа
def login_page():
    login_page = 'https://stellarburgers.nomoreparties.site/login'
    return login_page


@pytest.fixture  # главная страница
def main_page():
    main_page = 'https://stellarburgers.nomoreparties.site/'
    return main_page


@pytest.fixture  # страница регистрации
def registration_page():
    registration_page = 'https://stellarburgers.nomoreparties.site/register'
    return registration_page


@pytest.fixture()  # драйвер для setup и teardown браузера
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()
