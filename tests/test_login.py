from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from locators import Locators


def test_login_on_main_page(email, corr_password, main_page_driver, main_page):
    WebDriverWait(main_page_driver, 3).until(expected_conditions.visibility_of_element_located(Locators.LOGO_BUTTON))
    main_page_driver.find_element(*Locators.MAIN_PAGE_LOG_IN_BUTTON).click()
    main_page_driver.find_element(*Locators.EMAIL_FIELD).send_keys(email)
    main_page_driver.find_element(*Locators.PASSWORD_FIELD).send_keys(corr_password)
    main_page_driver.find_element(*Locators.LOGIN_BUTTON).click()
    WebDriverWait(main_page_driver, 10).until(expected_conditions.visibility_of_element_located(Locators.CHECKOUT_BUTTON))
    assert main_page_driver.current_url == main_page
    assert expected_conditions.visibility_of_element_located(Locators.CHECKOUT_BUTTON)


def test_login_via_personal_account(main_page_driver, main_page, email, corr_password):
    WebDriverWait(main_page_driver, 3).until(expected_conditions.visibility_of_element_located(Locators.LOGO_BUTTON))
    main_page_driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()
    main_page_driver.find_element(*Locators.EMAIL_FIELD).send_keys(email)
    main_page_driver.find_element(*Locators.PASSWORD_FIELD).send_keys(corr_password)
    main_page_driver.find_element(*Locators.LOGIN_BUTTON).click()
    WebDriverWait(main_page_driver, 3).until(expected_conditions.visibility_of_element_located(Locators.CHECKOUT_BUTTON))
    assert main_page_driver.current_url == main_page
    assert expected_conditions.visibility_of_element_located(Locators.CHECKOUT_BUTTON)


def test_login_via_registration_form(email, corr_password, registration_page, main_page, registration_page_driver):
    WebDriverWait(registration_page_driver, 3).until(expected_conditions.visibility_of_element_located(Locators.REGISTRATION_BUTTON))
    registration_page_driver.find_element(*Locators.REGISTRATION_AND_RECOVERY_FORM_LOG_IN_BUTTON).click()
    registration_page_driver.find_element(*Locators.EMAIL_FIELD).send_keys(email)
    registration_page_driver.find_element(*Locators.PASSWORD_FIELD).send_keys(corr_password)
    registration_page_driver.find_element(*Locators.LOGIN_BUTTON).click()
    WebDriverWait(registration_page_driver, 3).until(expected_conditions.visibility_of_element_located(Locators.CHECKOUT_BUTTON))
    assert registration_page_driver.current_url == main_page
    assert expected_conditions.visibility_of_element_located(Locators.CHECKOUT_BUTTON)


def test_login_password_recovery_form(email, corr_password, login_page_driver, main_page):
    WebDriverWait(login_page_driver, 3).until(expected_conditions.visibility_of_element_located(Locators.LOG_IN_HEADER))
    login_page_driver.find_element(*Locators.RECOVERY_PASSWORD_BUTTON).click()
    login_page_driver.find_element(*Locators.REGISTRATION_AND_RECOVERY_FORM_LOG_IN_BUTTON).click()
    login_page_driver.find_element(*Locators.EMAIL_FIELD).send_keys(email)
    login_page_driver.find_element(*Locators.PASSWORD_FIELD).send_keys(corr_password)
    login_page_driver.find_element(*Locators.LOGIN_BUTTON).click()
    WebDriverWait(login_page_driver, 3).until(expected_conditions.visibility_of_element_located(Locators.CHECKOUT_BUTTON))
    assert login_page_driver.current_url == main_page
    assert expected_conditions.visibility_of_element_located(Locators.CHECKOUT_BUTTON)


def test_personal_account_button_click(login_page, main_page_driver):
    WebDriverWait(main_page_driver, 3).until(expected_conditions.visibility_of_element_located(Locators.LOGO_BUTTON))
    main_page_driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()
    assert main_page_driver.current_url == login_page


def test_constructor_button_click_via_personal_account(login_page_driver, main_page):
    WebDriverWait(login_page_driver, 3).until(expected_conditions.visibility_of_element_located(Locators.LOGO_BUTTON))
    login_page_driver.find_element(*Locators.CONSTRUCTOR_BUTTON).click()
    assert login_page_driver.current_url == main_page


def test_logo_button_click_via_personal_account(login_page_driver, main_page):
    WebDriverWait(login_page_driver, 3).until(expected_conditions.visibility_of_element_located(Locators.LOGO_BUTTON))
    login_page_driver.find_element(*Locators.LOGO_BUTTON).click()
    assert login_page_driver.current_url == main_page


def test_logout_via_personal_account(email, corr_password, login_page_driver, login_page):
    WebDriverWait(login_page_driver, 3).until(expected_conditions.visibility_of_element_located(Locators.LOGO_BUTTON))
    login_page_driver.find_element(*Locators.EMAIL_FIELD).send_keys(email)
    login_page_driver.find_element(*Locators.PASSWORD_FIELD).send_keys(corr_password)
    login_page_driver.find_element(*Locators.LOGIN_BUTTON).click()
    WebDriverWait(login_page_driver, 3).until(expected_conditions.visibility_of_element_located(Locators.LOGO_BUTTON))
    login_page_driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()
    WebDriverWait(login_page_driver, 3).until(expected_conditions.visibility_of_element_located(Locators.LOGOUT_BUTTON))
    login_page_driver.find_element(*Locators.LOGOUT_BUTTON).click()
    WebDriverWait(login_page_driver, 3).until(expected_conditions.visibility_of_element_located(Locators.LOGIN_BUTTON))
    assert login_page_driver.current_url == login_page
    assert expected_conditions.visibility_of_element_located(Locators.LOG_IN_HEADER)
