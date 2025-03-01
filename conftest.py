import pytest
import allure
from selenium import webdriver
from pages.main_page import MainPage
from urls import URLS


@allure.step('Открыть браузер, перейти на главную страницу / Закрыть браузер')
@pytest.fixture
def driver():

    driver = webdriver.Firefox()
    driver.get(URLS.MAIN_PAGE)
    driver.find_element(*MainPage.COOKIE_BUTTON).click()

    yield driver
    driver.quit()