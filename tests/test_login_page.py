import allure

from pages.main_page import MainPage
from pages.login_page import LoginPage


class TestLoginPage:
    """Класс с тестами для страницы авторизации."""

    @allure.title('Проверка ошибки при авторизации с неверными данными пользователя')
    @allure.description('''
        1. Фикстура auth_incorrect_user_data выполняет попытку входа с неверными данными;
        2. Проверка, что отображается сообщение об ошибке;
        3. Проверка отсутствия ошибок в логах браузера.
    ''')
    def test_login_incorrect_data_user(self, login_page: LoginPage, auth_incorrect_user_data) -> None:
        """
        - Тест проверяет отображение ошибки при попытке входа с неверными учетными данными;
        - Фикстура выполняет авторизацию до теста;
        - В логах браузера нет ошибок.

        :param login_page: экземпляр LoginPage,
        :param auth_incorrect_user_data: фикстура авторизации с неверными данными.
        """

        with allure.step('Проверить текст ошибки'):
            error_text = login_page.get_text_login_error()
            assert error_text == 'Некорректный пароль', f"Ожидалось 'Некорректный пароль', а вернулось '{error_text}'"

        with allure.step('Проверить отсутствие ошибок в логах браузера'):
            assert not login_page.has_browser_errors(), f"Найдены ошибки загрузки: {login_page.get_browser_error_messages()}"

    @allure.title('Проверка успешного входа')
    @allure.description('''
        1. Фикстура auth выполняет авторизацию (клик по кнопке 'Войти в аккаунт, ввод корректных данных пользователя);
        2. Проверка, что пользователь перенаправлен на главную страницу;
        3. Проверка отсутствия ошибок в логах браузера.
    ''')
    def test_login_correct_data_user(self, main_page: MainPage, auth_correct_user_data) -> None:
        """
        - Тест проверяет успешный вход в систему с корректными учетными данными;
        - Фикстура auth_correct_user_data выполняет авторизацию до теста.

        :param main_page: экземпляр MainPage,
        :param auth_correct_user_data: фикстура выполняет авторизацию на сайте.
        """
        with allure.step("Проверить, что главная страница загружена"):
            assert main_page.check_correct_main_page(), "Главная страница не загрузилась после входа"

        with allure.step('Проверить отсутствие ошибок в логах браузера'):
            assert not main_page.has_browser_errors(), f"Найдены ошибки загрузки: {main_page.get_browser_error_messages()}"
