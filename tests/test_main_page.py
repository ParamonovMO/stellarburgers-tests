import allure

from pages.main_page import MainPage
from pages.login_page import LoginPage


class TestMainPage:
    """Класс с тестами для главной страницы сервиса."""

    @allure.title('Проверка корректного отображения главной страницы')
    @allure.description('''
        1. Фикстура автоматически открывает главную страницу;
        2. Проверка отображения всех элементов главной страницы;
        3. Проверка текущего URL страницы.
    ''')
    def test_check_correct_page_display(self, main_page: MainPage) -> None:
        """
        Тест проверяет, что главная страница отображается корректно:
        - URL соответствует ожидаемому,
        - все основные элементы (хедер, кнопки, формы, корзина) видны.

        :param main_page: фикстура с экземпляром главной страницы.
        """
        with allure.step('Проверить корректность отображения главной страницы'):
            assert main_page.check_correct_url(), 'URL не соответствует главной странице'
            assert main_page.check_all_elements(), 'Не все основные элементы видны'
            assert main_page.check_login_btn(), 'Кнопка "Войти в аккаунт" не отображается'

    @allure.title('Проверка перехода к странице логина')
    @allure.description('''
        1. Переход на главную страницу;
        2. Клик по кнопке 'Войти в аккаунт';
        3. Проверка текущего URL;
        4. Проверка отображения формы авторизации.
    ''')
    def test_click_login_btn_and_check_transition_login_page(self, main_page: MainPage, login_page: LoginPage) -> None:
        """
        Тест проверяет переход на страницу авторизации:
        - клик по кнопке 'Войти в аккаунт',
        - URL соответствует ожидаемому,
        - форма авторизации отображена.

        :param main_page: фикстура с экземпляром главной страницы.
        :param login_page: фикстура с экземпляром страницы авторизации.
        """
        with allure.step("Нажать на кнопку 'Войти в аккаунт'"):
            main_page.login_btn_click()

        with allure.step("Проверить, что открыта страница логина"):
            assert login_page.check_correct_url(), "URL не соответствует странице логина"
            assert login_page.check_auth_form_visible(), "Форма авторизации не отображается"
