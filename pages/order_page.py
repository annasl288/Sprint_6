from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import allure

class OrderPage(BasePage):
    NAME = (By.XPATH, ".//input[@placeholder = '* Имя']")  # Поле ввода имени
    SURNAME = (By.XPATH, ".//input[@placeholder = '* Фамилия']")  # Поле ввода фамилии
    ADDRESS = (By.XPATH, ".//input[contains(@placeholder, '* Адрес')]")  # Поле ввода адреса
    METRO = (By.XPATH, ".//input[@placeholder = '* Станция метро']")  # Поле ввода станции метро
    METRO_STATION = (By.XPATH, ".//div[text() = 'Парк культуры']")  # Выбор тестовой станции метро
    PHONE = (By.XPATH, ".//input[contains(@placeholder, '* Телефон')]")  # Поле ввода телефона
    DATE = (By.XPATH, ".//input[@placeholder = '* Когда привезти самокат']")  # Поле ввода даты
    PICK_DATE = (By.XPATH, ".//div[@aria-label = 'Choose пятница, 28-е февраля 2025 г.']")  # Выбор тестовой дата
    DAYS = (By.XPATH, ".//div[text() = '* Срок аренды']")  # Выбор срока аренды
    RENT_THREE_DAYS = (By.XPATH, ".//div[text() = 'трое суток']")  # Выбор тестового срока аренды

    NEXT_BUTTON = (By.XPATH, ".//button[text() = 'Далее']")  # Кнопка "Далее"
    ORDER_BUTTON = (By.XPATH, ".//button[text() = 'Заказать' and contains(@class, 'Button_Middle')]")  # Кнопка "Заказать"

    CONFIRMATION_HEADER = (By.XPATH, ".//div[contains(@class, 'Order_ModalHeader')]")  # Заголовок поп-апа с подтверждением заказа
    CONFIRMATION_BUTTON = (By.XPATH, ".//button[text() = 'Да']")  # Кнопка "Да"

    ORDER_CONFIRMED_HEADER = (By.XPATH, ".//div[contains(@class, 'Order_ModalHeader')]")  # Заголовок поп-апа "Заказ оформлен"

    @allure.step('Заполнить поля формы тестовыми данными о пользователе')
    def fill_out_form_about_user(self, user):
        self.get_element(self.NAME).send_keys(user['name'])
        self.get_element(self.SURNAME).send_keys(user['surname'])
        self.get_element(self.ADDRESS).send_keys(user['address'])
        self.get_element(self.METRO).click()
        self.get_element(self.METRO).send_keys(user['metro'])
        self.get_element(self.METRO_STATION).click()
        self.get_element(self.PHONE).send_keys(user['phone'])

    @allure.step('Заполнить поля формы тестовыми данными об аренде')
    def fill_out_form_about_rent(self, user):
        self.get_element(self.DATE).send_keys(user['date'])
        self.get_element(self.PICK_DATE).click()
        self.get_element(self.DAYS).click()
        self.get_element(self.RENT_THREE_DAYS).click()

    @allure.step('Заполнить форму заказа')
    def fill_out_order_form(self, user):
        self.fill_out_form_about_user(user)
        self.get_element(self.NEXT_BUTTON).click()
        self.fill_out_form_about_rent(user)
        self.get_element(self.ORDER_BUTTON).click()

    @allure.step('Нажать на кнопку "Да" для подтверждения заказа')
    def confirm_order(self):
        self.get_element(self.CONFIRMATION_BUTTON).click()