from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from locators import Locators


def test_bread_section_click(main_page_driver):
    WebDriverWait(main_page_driver, 3).until(expected_conditions.visibility_of_element_located(Locators.LOGO_BUTTON))
    main_page_driver.find_element(*Locators.SAUCES_SECTION).click()
    main_page_driver.find_element(*Locators.BREAD_SECTION).click()
    assert main_page_driver.find_element(*Locators.BREAD_SECTION_ACTIVE)


def test_sauces_section_click(main_page_driver):
    WebDriverWait(main_page_driver, 3).until(expected_conditions.visibility_of_element_located(Locators.LOGO_BUTTON))
    main_page_driver.find_element(*Locators.SAUCES_SECTION).click()
    assert main_page_driver.find_element(*Locators.SAUCES_SECTION_ACTIVE)


def test_fillings_section_click(main_page_driver):
    WebDriverWait(main_page_driver, 3).until(expected_conditions.visibility_of_element_located(Locators.LOGO_BUTTON))
    main_page_driver.find_element(*Locators.FILLINGS_SECTION).click()
    assert main_page_driver.find_element(*Locators.FILLINGS_SECTION_ACTIVE)
