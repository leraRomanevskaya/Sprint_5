from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from locators import Locators


def test_login_on_main_page(email, corr_password, main_page):
    driver = webdriver.Chrome()
    driver.get(main_page)
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.LOGO_BUTTON))
    driver.find_element(*Locators.MAIN_PAGE_LOG_IN_BUTTON).click()
    driver.find_element(*Locators.EMAIL_FIELD).send_keys(email)
    driver.find_element(*Locators.PASSWORD_FIELD).send_keys(corr_password)
    driver.find_element(*Locators.LOGIN_BUTTON).click()
    WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(Locators.CHECKOUT_BUTTON))
    assert driver.current_url == main_page
    assert expected_conditions.visibility_of_element_located(Locators.CHECKOUT_BUTTON)
    driver.quit()


def test_login_via_personal_account(email, corr_password, main_page):
    driver = webdriver.Chrome()
    driver.get(main_page)
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.LOGO_BUTTON))
    driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()
    driver.find_element(*Locators.EMAIL_FIELD).send_keys(email)
    driver.find_element(*Locators.PASSWORD_FIELD).send_keys(corr_password)
    driver.find_element(*Locators.LOGIN_BUTTON).click()
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.CHECKOUT_BUTTON))
    assert driver.current_url == main_page
    assert expected_conditions.visibility_of_element_located(Locators.CHECKOUT_BUTTON)
    driver.quit()


def test_login_via_registration_form(email, corr_password, registration_page, main_page):
    driver = webdriver.Chrome()
    driver.get(registration_page)
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.REGISTRATION_BUTTON))
    driver.find_element(*Locators.REGISTRATION_AND_RECOVERY_FORM_LOG_IN_BUTTON).click()
    driver.find_element(*Locators.EMAIL_FIELD).send_keys(email)
    driver.find_element(*Locators.PASSWORD_FIELD).send_keys(corr_password)
    driver.find_element(*Locators.LOGIN_BUTTON).click()
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.CHECKOUT_BUTTON))
    assert driver.current_url == main_page
    assert expected_conditions.visibility_of_element_located(Locators.CHECKOUT_BUTTON)
    driver.quit()


def test_login_password_recovery_form(email, corr_password, login, main_page):
    driver = webdriver.Chrome()
    driver.get(login)
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.LOG_IN_HEADER))
    driver.find_element(*Locators.RECOVERY_PASSWORD_BUTTON).click()
    driver.find_element(*Locators.REGISTRATION_AND_RECOVERY_FORM_LOG_IN_BUTTON).click()
    driver.find_element(*Locators.EMAIL_FIELD).send_keys(email)
    driver.find_element(*Locators.PASSWORD_FIELD).send_keys(corr_password)
    driver.find_element(*Locators.LOGIN_BUTTON).click()
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.CHECKOUT_BUTTON))
    assert driver.current_url == main_page
    assert expected_conditions.visibility_of_element_located(Locators.CHECKOUT_BUTTON)
    driver.quit()


def test_personal_account_button_click(login, main_page):
    driver = webdriver.Chrome()
    driver.get(main_page)
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.LOGO_BUTTON))
    driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()
    assert driver.current_url == login
    driver.quit()


def test_constructor_button_click_via_personal_account(login, main_page):
    driver = webdriver.Chrome()
    driver.get(login)
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.LOGO_BUTTON))
    driver.find_element(*Locators.CONSTRUCTOR_BUTTON).click()
    assert driver.current_url == main_page
    driver.quit()


def test_logo_button_click_via_personal_account(login, main_page):
    driver = webdriver.Chrome()
    driver.get(login)
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.LOGO_BUTTON))
    driver.find_element(*Locators.LOGO_BUTTON).click()
    assert driver.current_url == main_page
    driver.quit()


def test_logout_via_personal_account(email, corr_password, login):
    driver = webdriver.Chrome()
    driver.get(login)
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.LOGO_BUTTON))
    driver.find_element(*Locators.EMAIL_FIELD).send_keys(email)
    driver.find_element(*Locators.PASSWORD_FIELD).send_keys(corr_password)
    driver.find_element(*Locators.LOGIN_BUTTON).click()
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.LOGO_BUTTON))
    driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.LOGOUT_BUTTON))
    driver.find_element(*Locators.LOGOUT_BUTTON).click()
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.LOGIN_BUTTON))
    assert driver.current_url == login
    driver.quit()
