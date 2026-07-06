from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.remote.webelement import WebElement
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.remote.webdriver import WebDriver


class BasePage:
    """
    Базовый класс для всех страниц приложения.
    Содержит методы для взаимодействия с веб-элементами.
    """

    def __init__(self, driver: WebDriver) -> None:
        """
	    Инициализация базовой страницы.
        :param driver: экземпляр WebDriver.
        """
        self.driver = driver
        self.timeout = 5

# ---------- Вспомогательные приватные методы ----------

    def _wait_element_clickable(self, locator: tuple[str, str]) -> WebElement:
        """
	    Метод ожидает, пока элемент станет кликабельным.
        :param locator: кортеж (By, значение);
        :return WebElement - кликабельный элемент.
        """
        return WebDriverWait(self.driver, self.timeout).until(EC.element_to_be_clickable(locator))

    def _wait_element_visible(self, locator: tuple[str, str]) -> WebElement:
        """
	    Метод ожидает, пока элемент станет видимым.
        :param locator: кортеж (By, значение);
        :return WebElement - видимый элемент.
        """
        return WebDriverWait(self.driver, self.timeout).until(EC.visibility_of_element_located(locator))

# ---------- Методы взаимодействия ----------

    def get_current_url(self) -> str:
        """
	    Метод возвращает текущий URL страницы
	    :return: строка с текущим URL.
	    """
        return self.driver.current_url

    def wait_for_url(self, expected_url: str) -> None:
        """
	    Метод ожидает изменение текущего URL к заявленному.
        :param expected_url: ожидаемый URL.
        """
        WebDriverWait(self.driver, self.timeout).until(EC.url_to_be(expected_url))

    def click_button(self, locator: tuple[str, str]) -> None:
        """
	    Метод кликает по кнопке.
        :param locator: кортеж (By, значение).
        """
        element = self._wait_element_clickable(locator)
        element.click()

    def send_keys_to_field(self, locator: tuple[str, str], text: str) -> None:
        """
	    Метод очищает поле ввода и вводит указанный текст.
        :param locator: кортеж (By, значение);
	    :param text: текст для ввода.
        """
        element = self._wait_element_clickable(locator)
        element.clear()
        element.send_keys(text)

    def is_element_visible(self, locator: tuple[str, str]) -> bool:
        """
	    Метод проверяет, видно ли элемент на странице.
        :param locator: кортеж (By, значение);
        :return True, если элемент видим, если нет, то возвращает False.
        """
        try:
            self._wait_element_visible(locator)
            return True
        except TimeoutException:
            return False

    def get_element_text(self, locator: tuple[str, str]) -> str | None:
        """
	    Метод ожидает видимости элемента и возвращает его текст.
        :param locator: кортеж (By, значение);
        :return: текст, если элемент не найден, возвращает None.
        """
        try:
            element = self._wait_element_visible(locator)
            return element.text
        except TimeoutException:
            return None

    def check_url(self, expected_url: str) -> bool:
        """
        Проверяет, что текущий URL совпадает с ожидаемым URL главной страницы.
        :param expected_url: ожидаемый URL,
        :return: True, если URL совпадает, иначе False.
        """
        return self.get_current_url() == expected_url
