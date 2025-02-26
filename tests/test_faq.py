from pages.main_page import MainPage
import pytest
import allure

class TestFAQ:

    @allure.title('Текст ответов в разделе "Вопросы о важном" соответствует заданному')
    @pytest.mark.parametrize ('question, answer, expected_answer', zip(MainPage.questions, MainPage.answers, MainPage.expected_answers))
    def test_faq(self, driver, question, answer, expected_answer):
        main_page = MainPage(driver)

        main_page.scroll_to_faq(question)
        main_page.click_question(question)

        text = main_page.get_element(answer).text
        assert text == expected_answer