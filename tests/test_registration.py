from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from locators import Locators


def test_registration_is_correct(name, random_email, random_corr_password, login_page, registration_page_driver):
    registration_page_driver.find_element(*Locators.REGISTRATION_FIELD_NAME).send_keys(name)
    registration_page_driver.find_element(*Locators.REGISTRATION_FIELD_EMAIL).send_keys(random_email)
    registration_page_driver.find_element(*Locators.REGISTRATION_FIELD_PASSWORD).send_keys(random_corr_password)
    registration_page_driver.find_element(*Locators.REGISTRATION_BUTTON).click()
    WebDriverWait(registration_page_driver, 3).until(expected_conditions.visibility_of_element_located(Locators.LOG_IN_HEADER))
    assert registration_page_driver.current_url == login_page


def test_registration_uncorrect_password(name, random_email, uncorr_password, registration_page_driver):
    registration_page_driver.find_element(*Locators.REGISTRATION_FIELD_NAME).send_keys(name)
    registration_page_driver.find_element(*Locators.REGISTRATION_FIELD_EMAIL).send_keys(random_email)
    registration_page_driver.find_element(*Locators.REGISTRATION_FIELD_PASSWORD).send_keys(uncorr_password)
    registration_page_driver.find_element(*Locators.REGISTRATION_BUTTON).click()
    assert registration_page_driver.find_element(*Locators.UNCORR_PASSWORD).text == 'Некорректный пароль'
