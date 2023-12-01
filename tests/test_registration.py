from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from locators import Locators


def test_registration_is_correct(name, random_email, random_corr_password, login, registration_page):
    driver = webdriver.Chrome()
    driver.get(registration_page)
    driver.find_element(*Locators.REGISTRATION_FIELD_NAME).send_keys(name)
    driver.find_element(*Locators.REGISTRATION_FIELD_EMAIL).send_keys(random_email)
    driver.find_element(*Locators.REGISTRATION_FIELD_PASSWORD).send_keys(random_corr_password)
    driver.find_element(*Locators.REGISTRATION_BUTTON).click()
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.LOG_IN_HEADER))
    assert driver.current_url == login
    driver.quit()


def test_registration_uncorrect_password(name, random_email, uncorr_password, registration_page):
    driver = webdriver.Chrome()
    driver.get(registration_page)
    driver.find_element(*Locators.REGISTRATION_FIELD_NAME).send_keys(name)
    driver.find_element(*Locators.REGISTRATION_FIELD_EMAIL).send_keys(random_email)
    driver.find_element(*Locators.REGISTRATION_FIELD_PASSWORD).send_keys(uncorr_password)
    driver.find_element(*Locators.REGISTRATION_BUTTON).click()
    assert driver.find_element(*Locators.UNCORR_PASSWORD).text == 'Некорректный пароль'
    driver.quit()
