import allure

from pages.base_page import BasePage
from locators.locators import MainPageLocators
from data.urls import Urls


class MainPage(BasePage):
    """Класс для работы с главной страницей."""

    @allure.step('Проверка отображения хедера')
    def check_header_form(self) -> bool:
        """
        Метод проверяет отображение хедера на главной странице.

        :return: True, если хедер виден, иначе False.
        """
        return self.is_element_visible(MainPageLocators.header_form)

    @allure.step('Проверка отображения кнопки "Конструктор"')
    def check_constructor_btn(self) -> bool:
        """
        Метод проверяет отображение кнопки 'Конструктор' на главной странице.

        :return: True, если кнопка видна, иначе False.
        """
        return self.is_element_visible(MainPageLocators.constructor_btn)

    @allure.step('Проверка отображения кнопки "Лента Заказов"')
    def check_orders_feed_form(self) -> bool:
        """
        Метод проверяет отображение кнопки 'Лента Заказов' на главной странице.

        :return: True, если кнопка видна, иначе False.
        """
        return self.is_element_visible(MainPageLocators.order_feed_btn)

    @allure.step('Проверка отображения кнопки "Личный кабинет"')
    def check_personal_account_btn(self) -> bool:
        """
        Метод проверяет отображение кнопки 'Личный кабинет' на главной странице.

        :return: True, если кнопка видна, иначе False.
        """
        return self.is_element_visible(MainPageLocators.personal_area_btn)

    @allure.step('Проверка отображения заголовка')
    def check_title_form(self) -> bool:
        """
        Метод проверяет отображение заголовка на главной странице.

        :return: True, если заголовок виден, иначе False.
        """
        return self.is_element_visible(MainPageLocators.title_main_page)

    @allure.step('Проверка отображения формы ингредиентов')
    def check_ingredients_form(self) -> bool:
        """
        Метод проверяет отображение формы ингредиентов на главной странице.

        :return: True, если форма видна, иначе False.
        """
        return self.is_element_visible(MainPageLocators.ingredients_form)

    @allure.step('Проверка отображения верхней булочки')
    def check_top_bun_form(self) -> bool:
        """
        Метод проверяет отображение верхней булочки в конструкторе.

        :return: True, если элемент виден, иначе False.
        """
        return self.is_element_visible(MainPageLocators.constructor_top_bun)

    @allure.step('Проверка отображения нижней булочки')
    def check_bottom_bun_form(self) -> bool:
        """
        Метод проверяет отображение нижней булочки в конструкторе.

        :return: True, если элемент виден, иначе False.
        """
        return self.is_element_visible(MainPageLocators.constructor_top_bottom)

    @allure.step('Проверка отображения корзины')
    def check_basket_form(self) -> bool:
        """
        Метод проверяет отображение корзины на главной странице.

        :return: True, если корзина видна, иначе False.
        """
        return self.is_element_visible(MainPageLocators.basket_form)

    @allure.step('Проверка отображения кнопки "Войти в аккаунт"')
    def check_login_btn(self) -> bool:
        """
        Метод проверяет отображение кнопки на главной странице.

        :return True, если кнопка видна, иначе False.
        """
        return self.is_element_visible(MainPageLocators.login_account_btn)

    @allure.step('Проверка текущего URL страницы')
    def check_correct_url(self) -> bool:
        """
        Метод проверяет, что текущий URL совпадает с ожидаемым URL главной страницы.

        :return: True, если URL совпадает, иначе False.
        """
        return self.check_url(Urls.MAIN_URL)

    @allure.step('Проверка всех элементов главной страницы')
    def check_all_elements(self) -> bool:
        """
        Метод проверяет видимость всех ключевых элементов на главной странице.
        Проверяются: хедер, кнопки, заголовок, формы, булочки, корзина.

        :return: True, если все элементы видны, иначе False.
        """
        return all([
            self.check_header_form(),
            self.check_constructor_btn(),
            self.check_orders_feed_form(),
            self.check_personal_account_btn(),
            self.check_title_form(),
            self.check_ingredients_form(),
            self.check_top_bun_form(),
            self.check_bottom_bun_form(),
            self.check_basket_form()
        ])

    @allure.step('Проверка корректного отображения главной страницы')
    def check_correct_main_page(self) -> bool:
        """
        Метод проверяет полную корректность отображения главной страницы:
        - URL;
        - Все основные элементы.

        :return: True, если URL корректен и все элементы видны, иначе False.
        """
        return self.check_all_elements() and self.check_correct_url()

    @allure.step('Клик по кнопке "Войти в аккаунт"')
    def login_btn_click(self) -> None:
        """Метод выполняет клик по кнопке 'Войти в аккаунт'."""
        self.click_button(MainPageLocators.login_account_btn)

    @allure.step('Клик по кнопке "Личный кабинет"')
    def personal_area_btn_click(self) -> None:
        """Метод выполняет клик по кнопке 'Личный кабинет'."""
        self.click_button(MainPageLocators.personal_area_btn)
