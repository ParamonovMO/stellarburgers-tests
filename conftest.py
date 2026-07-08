import os

import allure

import pytest

from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.chrome.options import Options

from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.profile_page import ProfilePage
from data.urls import Urls
from helpers.user_data import PersonalData, IncorrectPersonalData

from collections.abc import Generator


@pytest.fixture()
def driver() -> Generator[WebDriver, None, None]:
    """
    Фикстура для инициализации и завершения работы драйвера.
    - Локально: запускает браузер с графическим интерфейсом.
    - В CI: автоматически включает headless.
    - Открывает браузер Chrome c разрешением 1920*1080.
    - Переходит на главную страницу сервиса.
    - После выполнения теста браузер закрывается.

    :yield экземпляр WebDriver.
    """
    with allure.step("Открыть браузер Chrome и перейти на главную страницу"):
        options = Options()
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")

        if os.getenv('CI') == 'true':
            options.add_argument("--headless")

        driver = webdriver.Chrome(options=options)
        driver.set_window_size(1920, 1080)
        driver.get(Urls.MAIN_URL)
        yield driver
    
    with allure.step("Закрыть браузер"):
        driver.quit()

@pytest.fixture
def main_page(driver: WebDriver) -> MainPage:
    """
    Фикстура для создания экземпляра главной страницы.
    :param driver: экземпляр WebDriver.
    :return объект MainPage
    """
    return MainPage(driver)

@pytest.fixture
def login_page(driver: WebDriver) -> LoginPage:
    """
    Фикстура для создания экземпляра страницы авторизации.
    :param driver: экземпляр WebDriver.
    :return объект LoginPage
    """
    return LoginPage(driver)

@pytest.fixture
def profile_page(driver: WebDriver) -> ProfilePage:
    """
    Фикстура для создания экземпляра страницы личного кабинета.
    :param driver: экземпляр WebDriver.
    :return объект ProfilePage
    """
    return ProfilePage(driver)

@pytest.fixture
def auth_correct_user_data(main_page: MainPage, login_page: LoginPage) -> None:
    """
    Фикстура выполняет авторизацию под действующим пользователем;
    Использует фикстуры main_page, login_page для выполнения авторизации;
    После входа ждет перенаправление на главную страницу.

    :param main_page: фикстура главной страницы,
    :param login_page: фикстура страницы авторизации.
    """
    with allure.step('Авторизация под действующим пользователем'):
        main_page.login_btn_click()
        login_page.login(
            PersonalData.USER_EMAIL,
            PersonalData.USER_PASSWORD
        )
        main_page.wait_for_url(Urls.MAIN_URL)

@pytest.fixture
def auth_incorrect_user_data(main_page: MainPage, login_page: LoginPage) -> None:
    """
    Фикстура выполняет авторизацию под некорретными данными пользователя.
    После ввода данных остается на странице авторизации с сообщением об ошибке.

    :param main_page: фикстура главной страницы,
    :param login_page: фикстура страницы авторизации.
    """
    with allure.step('Попытка авторизации под неверными учетными данными'):
        main_page.login_btn_click()
        login_page.login(
            IncorrectPersonalData.USER_EMAIL,
            IncorrectPersonalData.USER_PASSWORD
        )
