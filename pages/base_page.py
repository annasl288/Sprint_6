from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import allure

class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def go_to_new_tab(self):
        self.driver.switch_to.window(self.driver.window_handles[1])

    def get_element(self, locator):
        return self.driver.find_element(*locator)

    def scroll_to_element(self, locator):
        element = self.get_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def wait_for_clickable_element(self, locator):
        WebDriverWait(self.driver, 3).until(expected_conditions.element_to_be_clickable(locator))

    def get_current_url(self):
        return self.driver.current_url


class Header(BasePage):

    SCOOTER_LOGO = (By.XPATH, ".//img[@alt = 'Scooter']")  # Логотип Самоката
    YANDEX_LOGO = (By.XPATH, ".//img[@alt = 'Yandex']")  # Логотип Яндекса
    DZEN_MAIN_BUTTON = (By.XPATH, ".//span[text() = 'Главная']")  # Кнопка "Главная" на dzen.ru
    ORDER_BUTTON = (By.XPATH, ".//button[text() = 'Заказать'][1]")  # Кнопка "Заказать" в шапке страницы

    @allure.step('Нажать на кнопку "Заказать" в шапке страницы')
    def click_order_button(self):
        self.get_element(self.ORDER_BUTTON).click()

    @allure.step('Нажать на лого Самоката в шапке страницы')
    def click_scooter_logo(self):
        self.get_element(self.SCOOTER_LOGO).click()

    @allure.step('Нажать на лого Яндекса в шапке страницы')
    def click_yandex_logo(self):
        self.get_element(self.YANDEX_LOGO).click()

    def wait_for_dzen_page(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.presence_of_element_located(self.DZEN_MAIN_BUTTON))