import allure

from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.profile_page import ProfilePage
from data.urls import Urls


class TestProfilePage:
    """Класс с тестами для страницы профиля."""

    @allure.title('Проверка успешного выхода из профиля')
    @allure.description('''
        1. Фикстура auth_correct_user_data выполняет авторизацию (клик по кнопке 'Войти в аккаунт, ввод корректных данных пользователя);
        2. Перейти в личный кабинет;
        3. Проверка отображения формы профиля и текущий URL;
        4. Нажать на кнопку выхода;
        5. Проверка переход на страницу логина;
        6. Проверка отсутствия ошибок в логах браузера.
    ''')
    def test_logout(self, main_page: MainPage, login_page: LoginPage, profile_page: ProfilePage, auth_correct_user_data) -> None:
        """
        Тест проверяет успешный выход из профиля:
        - Авторизация,
        - Переход в личный кабинет,
        - Клик по кнопке 'Выход',
        - Перенаправление на страницу логина.

        :param main_page: экземпляр MainPage,
        :param login_page: экземпляр LoginPage,
        :param profile_page: экземпляр ProfilePage,
        :param auth_correct_user_data: фикстура выполняет авторизацию на сайте.
        """
        with allure.step("Перейти на страницу профиля"):
            main_page.personal_area_btn_click()

        with allure.step("Проверить отображение формы профиля и текущий URL"):
            assert profile_page.check_personal_area_form(), "Форма личного кабинета не отображается"
            assert profile_page.check_correct_url(), 'URL не соответствует странице профиля'

        with allure.step("Нажать на кнопку 'Выход'"):
            profile_page.logout_btn_click()

        with allure.step("Проверить переход на страницу логина"):
            login_page.wait_for_url(Urls.LOGIN_URL)
            assert login_page.check_auth_form_visible(), "Форма авторизации не отображается после выхода"

        with allure.step('Проверить отсутствие ошибок в логах браузера'):
            assert not login_page.has_browser_errors(), f"Ошибка при загрузке страницы: {login_page.get_browser_error_messages()}"
