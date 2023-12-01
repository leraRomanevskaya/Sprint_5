from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from locators import Locators


def test_bread_section_click(main_page):
    driver = webdriver.Chrome()
    driver.get(main_page)
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.LOGO_BUTTON))
    driver.find_element(*Locators.SAUCES_SECTION).click()
    driver.find_element(*Locators.BREAD_SECTION).click()
    assert driver.find_element(*Locators.BREAD_SECTION_ACTIVE)
    driver.quit()


def test_sauces_section_click(main_page):
    driver = webdriver.Chrome()
    driver.get(main_page)
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.LOGO_BUTTON))
    driver.find_element(*Locators.SAUCES_SECTION).click()
    assert driver.find_element(*Locators.SAUCES_SECTION_ACTIVE)
    driver.quit()


def test_fillings_section_click(main_page):
    driver = webdriver.Chrome()
    driver.get(main_page)
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.LOGO_BUTTON))
    driver.find_element(*Locators.FILLINGS_SECTION).click()
    assert driver.find_element(*Locators.FILLINGS_SECTION_ACTIVE)
    driver.quit()
