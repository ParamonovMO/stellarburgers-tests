import allure

from pages.base_page import BasePage
from locators.locators import LoginPageLocators
from data.urls import Urls


class LoginPage(BasePage):
    """Класс для работы со страницей авторизации."""

    @allure.step('Проверка отображения формы логина')
    def check_auth_form_visible(self) -> bool:
        """
        Метод проверяет отображение формы авторизации на странице.

        :return: True, если форма видна, иначе False.
        """
        return self.is_element_visible(LoginPageLocators.auth_form)

    @allure.step('Проверка текущего URL страницы')
    def check_correct_url(self) -> bool:
        """
        Метод проверяет, что текущий URL совпадает с ожидаемым URL страницы логина.

        :return: True, если URL совпадает, иначе False.
        """
        return self.check_url(Urls.LOGIN_URL)

    @allure.step('Заполнение поля "Email"')
    def send_email_to_email_field(self, email: str) -> None:
        """
        Метод вводит указанный email в поле ввода электронной почты.

        :param email: адрес электронной почты.
        """
        self.send_keys_to_field(LoginPageLocators.email_input, email)

    @allure.step('Заполнение поля "Password"')
    def send_password_to_password_field(self, password: str) -> None:
        """
        Метод вводит указанный пароль в поле ввода пароля.

        :param password: пароль.
        """
        self.send_keys_to_field(LoginPageLocators.password_input, password)

    @allure.step('Клик на кнопку "Войти"')
    def click_login_btn(self) -> None:
        """Метод выполняет клик по кнопке 'Войти'."""
        self.click_button(LoginPageLocators.login_account_btn)

    @allure.step('Авторизация на сайте')
    def login(self, email: str, password: str) -> None:
        """
        Метод выполняет полную авторизацию на сайте.

        :param email: адрес электронной почты;
        :param password: пароль.
        """
        self.send_email_to_email_field(email)
        self.send_password_to_password_field(password)
        self.click_login_btn()

    @allure.step('Получение текста ошибки при некорректной авторизации')
    def get_text_login_error(self) -> str | None:
        """
        Метод возвращает текст сообщения об ошибке, если оно отображается.

        :return: текст ошибки или None, если ошибка не найдена.
        """
        return self.get_element_text(LoginPageLocators.text_login_error)
