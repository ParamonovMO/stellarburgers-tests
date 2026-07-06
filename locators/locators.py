from selenium.webdriver.common.by import By


class MainPageLocators:
    """Локаторы главной страницы"""

    header_form = (By.XPATH, ".//header[contains(@class, 'AppHeader_header__X9aJA')]")                         # Хедер
    personal_area_btn = (By.XPATH, ".//p[text() = 'Личный Кабинет']")                                          # Кнопка личного кабинета
    constructor_btn = (By.XPATH, ".//p[text() = 'Конструктор']")                                               # Кнопка конструктора
    order_feed_btn = (By.XPATH, ".//p[text() = 'Лента Заказов']")                                              # Кнопка ленты заказов
    ingredients_form = (By.XPATH, ".//div[contains(@class, 'BurgerIngredients')]")                             # Форма ингредиентов
    basket_form = (By.XPATH, ".//div[contains(@class, 'BurgerConstructor_basket__container__2fUl3')]")         # Форма корзины
    constructor_top_bun = (By.XPATH, ".//div[contains(@class, 'constructor-element_pos_top')]")                # Форма конструктора верхней булочки
    constructor_top_bottom = (By.XPATH, ".//div[contains(@class, 'constructor-element_pos_bottom')]")          # Форма конструктора нижней булочки
    login_account_btn = (By.XPATH, ".//button[contains(text(), 'Войти в аккаунт')]")                           # Кнопка войти в аккаунт
    title_main_page = (By.XPATH, ".//h1[text() ='Соберите бургер']")                                           # Заголовок главной страницы


class LoginPageLocators:
    """Локаторы формы авторизации"""

    auth_form = (By.XPATH, ".//div[contains(@class, 'Auth_login__3hAey')]")                                    # Форма авторизации
    email_input = (By.XPATH, ".//input[contains(@name, 'name')]")                                              # Поле ввода email
    password_input = (By.XPATH, ".//input[contains(@name, 'Пароль')]")                                         # Поле ввода пароля
    login_account_btn = (By.XPATH, "//button[text() = 'Войти']")                                               # Кнопка войти
    text_login_error = (By.XPATH, ".//p[text() = 'Некорректный пароль']")                                      # Ошибка при вводе некорректных данных


class ProfilePageLocators:
    """Локаторы формы личного кабинета"""

    profile_form = (By.XPATH, ".//div[contains(@class, 'Account_account__vgk_w')]")                            # Форма личного кабинета
    exit_btn = (By.XPATH, ".//button[text() = 'Выход']")                                                       # Кнопка выход
