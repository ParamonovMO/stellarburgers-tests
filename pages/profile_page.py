import allure

from pages.base_page import BasePage
from locators.locators import ProfilePageLocators
from data.urls import Urls


class ProfilePage(BasePage):
    """Класс для работы со страницей профиля."""

    @allure.step('Проверка отображения формы личного кабинета')
    def check_personal_area_form(self) -> bool:
        """
        Проверяет отображение формы профиля.
        :return: True, если форма видна, иначе False.
        """
        return self.is_element_visible(ProfilePageLocators.profile_form)

    @allure.step('Проверка текущего URL страницы профиля')
    def check_correct_url(self) -> bool:
        """
        Проверяет, что текущий URL соответствует странице профиля.
        :return: True, если URL совпадает, иначе False.
        """
        return self.get_current_url() == Urls.PROFILE_URL

    @allure.step('Клик по кнопке "Выход"')
    def logout_btn_click(self) -> None:
        """Выполняет клик по кнопке 'Выход'."""
        self.click_button(ProfilePageLocators.exit_btn)
