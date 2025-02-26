from pages.base_page import Header
from urls import URLS
import allure

class TestHeader:

    @allure.title('Переход на главную страницу сервиса по клику на лого Самоката')
    def test_click_scooter_logo(self, driver):
        header = Header(driver)

        header.click_order_button()
        header.click_scooter_logo()

        assert driver.current_url == URLS.MAIN_PAGE

    @allure.title('Переход на главную страницу Дзена по клику на лого Яндекса')
    def test_click_yandex_logo(self, driver):
        header = Header(driver)

        header.click_yandex_logo()
        header.go_to_new_tab(header.DZEN_MAIN_BUTTON)

        assert driver.current_url == URLS.DZEN_PAGE