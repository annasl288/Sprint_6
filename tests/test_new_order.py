from pages.base_page import Header
from pages.main_page import MainPage
from pages.order_page import OrderPage
from data import Users
import allure


class TestNewOrder:

    @allure.title('Заказ самоката по клику на кнопку "Заказать" в шапке страницы')
    def test_order_click_button_in_header(self, driver):
        header = Header(driver)
        order_page = OrderPage(driver)

        header.click_order_button()
        order_page.fill_out_order_form(Users.user_1)
        order_page.confirm_order()

        assert driver.find_element(*OrderPage.ORDER_CONFIRMED_HEADER).is_displayed()

    @allure.title('Заказ самоката по клику на кнопку "Заказать" в середине главной страницы')
    def test_order_click_button_main_page(self, driver):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)

        main_page.click_order_button()
        order_page.fill_out_order_form(Users.user_2)
        order_page.confirm_order()

        assert driver.find_element(*OrderPage.ORDER_CONFIRMED_HEADER).is_displayed()