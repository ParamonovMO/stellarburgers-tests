import allure

from helpers import user_data
from pages.main_page import MainPage
from pages.login_page import LoginPage


class TestLoginPage:
    """Класс с тестами для страницы авторизации."""

    @allure.title('Проверка ошибки при авторизации с неверными данными пользователя')
    @allure.description('''
        1. Открыть главную страницу;
        2. Клик по кнопке "Войти в аккаунт";
        3. Ввести неверный email и пароль;
        4. Проверка, что отображается сообщение об ошибке;
        5. Проверка отсутствия ошибок в логах браузера.
    ''')
    def test_login_incorrect_data_user(self, main_page: MainPage, login_page: LoginPage) -> None:
        """
        - Тест проверяет отображение ошибки при попытке входа с неверными учетными данными;
        - В логах браузера нет ошибок.

        :param main_page: экземпляр MainPage;
        :param login_page: экземпляр LoginPage.
        """
        with allure.step("Перейти на страницу логина"):
            main_page.login_btn_click()

        with allure.step("Ввести неверные учетные данные"):
            login_page.login(
                user_data.IncorrectPersonalData.USER_EMAIL,
                user_data.IncorrectPersonalData.USER_PASSWORD
            )

        with allure.step('Проверить текст ошибки'):
            error_text = login_page.get_text_login_error()
            assert error_text == 'Некорректный пароль', f"Ожидалось 'Некорректный пароль', а вернулось '{error_text}'"

        with allure.step('Проверить отсутствие ошибок в логах браузера'):
            assert not login_page.has_browser_errors(), f"Найдены ошибки загрузки: {login_page.get_browser_error_messages()}"

    @allure.title('Проверка успешного входа')
    @allure.description('''
        1. Открыть главную страницу;
        2. Клик по кнопке "Войти в аккаунт";
        3. Ввести верные email и пароль;
        4. Проверка, что пользователь перенаправлен на главную страницу;
        5. Проверка отсутствия ошибок в логах браузера.
    ''')
    def test_login_correct_data_user(self, main_page: MainPage, login_page: LoginPage) -> None:
        """
        - Тест проверяет успешный вход в систему с корректными учетными данными;
        - В логах браузера нет ошибок.
    
        :param main_page: экземпляр MainPage,
        :param login_page: экземпляр LoginPage.
        """
        with allure.step("Перейти на страницу логина"):
            main_page.login_btn_click()

        with allure.step("Ввести верные учетные данные"):
            login_page.login(
                user_data.PersonalData.USER_EMAIL,
                user_data.PersonalData.USER_PASSWORD
            )

        with allure.step("Проверить, что главная страница загружена"):
            assert main_page.check_correct_main_page(), "Главная страница не загрузилась после входа"

        with allure.step('Проверить отсутствие ошибок в логах браузера'):
            assert not main_page.has_browser_errors(), f"Найдены ошибки загрузки: {main_page.get_browser_error_messages()}"
