import pytest
import allure
from selenium import webdriver
from urls import URLS
from pages.base_page import BasePage

@allure.step('Открыть браузер, перейти на главную страницу / Закрыть браузер')
@pytest.fixture
def driver():

    driver = webdriver.Firefox()
    driver.get(URLS.MAIN_PAGE)
    driver.find_element(*BasePage.COOKIE_BUTTON).click()

    yield driver
    driver.quit()