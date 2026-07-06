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
def main_page(driver) -> MainPage:
    """"
    Фикстура для создания экземпляра главной страницы.
    :param driver: экземпляр WebDriver.
    :return объект MainPage
    """
    return MainPage(driver)

@pytest.fixture
def login_page(driver) -> LoginPage:
    """"
    Фикстура для создания экземпляра страницы авторизации.
    :param driver: экземпляр WebDriver.
    :return объект LoginPage
    """
    return LoginPage(driver)

@pytest.fixture
def profile_page(driver) -> ProfilePage:
    """"
    Фикстура для создания экземпляра страницы личного кабинета.
    :param driver: экземпляр WebDriver.
    :return объект ProfilePage
    """
    return ProfilePage(driver)
