from selenium.webdriver.common.by import By
import allure

class BasePage:

    COOKIE_BUTTON = (By.XPATH, ".//button[contains(@class, 'App_CookieButton')]")  # Кнопка принятия куки

    def __init__(self, driver):
        self.driver = driver

    def go_to_new_tab(self):
        self.driver.switch_to.window(self.driver.window_handles[1])

class Header(BasePage):

    SCOOTER_LOGO = (By.XPATH, ".//img[@alt = 'Scooter']")  # Логотип Самоката
    YANDEX_LOGO = (By.XPATH, ".//img[@alt = 'Yandex']")  # Логотип Яндекса
    ORDER_BUTTON = (By.XPATH, ".//button[text() = 'Заказать'][1]")  # Кнопка "Заказать" в шапке страницы

    @allure.step('Нажать на кнопку "Заказать" в шапке страницы')
    def click_order_button(self):
        self.driver.find_element(*self.ORDER_BUTTON).click()

    @allure.step('Нажать на лого Самоката в шапке страницы')
    def click_scooter_logo(self):
        self.driver.find_element(*self.SCOOTER_LOGO).click()

    @allure.step('Нажать на лого Яндекса в шапке страницы')
    def click_yandex_logo(self):
        self.driver.find_element(*self.YANDEX_LOGO).click()