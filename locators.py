from selenium.webdriver.common.by import By


class Locators(object):
    """A class for all locators"""

    REGISTRATION_FIELD_NAME = (By.XPATH, './/fieldset[1]//input')  # поле "Имя" на странице регистрации
    REGISTRATION_FIELD_EMAIL = (By.XPATH, './/fieldset[2]/div/div/input')  # поле "e-mail" на странице регистрации
    REGISTRATION_FIELD_PASSWORD = (By.XPATH, './/fieldset[3]/div/div/input')  # поле "Пароль" на странице регистрации
    REGISTRATION_BUTTON = (By.XPATH, './/button[text() = "Зарегистрироваться"]')  # кнопка "Зарегистрироваться"
    LOG_IN_HEADER = (By.XPATH, './/h2[text()="Вход"]')  # заголовок "Вход" на странице входа
    UNCORR_PASSWORD = (By.CLASS_NAME, 'input__error')  # надпись "Некорректный пароль" на странице входа
    MAIN_PAGE_LOG_IN_BUTTON = (By.XPATH, './/main/section[2]/div/button')  # кнопка "Войти в аккаунт" на главной странице
    EMAIL_FIELD = (By.XPATH, './/fieldset[1]//input')  # поле "e-mail" на странице входа
    PASSWORD_FIELD = (By.XPATH, './/fieldset[2]/div/div/input')  # поле "Паспорт" на странице регистрации
    PERSONAL_ACCOUNT_BUTTON = (By.XPATH, './/nav/a')   # кнопка "Личный кабинет" на главной странице
    REGISTRATION_AND_RECOVERY_FORM_LOG_IN_BUTTON = (By.CLASS_NAME, 'Auth_link__1fOlj')  # кнопка "Войти" на странице регистрации и восстановления пароля
    RECOVERY_PASSWORD_BUTTON = (By.XPATH, './/main/div/div/p[2]/a')   # кнопка "Восстановить пароль" на странице входа
    CONSTRUCTOR_BUTTON = (By.XPATH, './/nav/ul/li[1]')  # кнопка "Конструктор" в хедере
    LOGO_BUTTON = (By.CLASS_NAME, 'AppHeader_header__logo__2D0X2')  # кнопка с логотипом в хедере
    LOGIN_BUTTON = (By.XPATH, './/button[text()="Войти"]')  # поле "e-mail" на странице регистрации
    LOGOUT_BUTTON = (By.XPATH, './/main/div/nav/ul/li[3]/button')  # кнопка "Выйти" в личном кабинете
    CHECKOUT_BUTTON = (By.XPATH, './/button[text()="Оформить заказ"]')  # кнопка "Оформить заказ" на главной странице
    BREAD_SECTION = (By.XPATH, './/section/div/div[1][contains(@class,"tab_tab__1SPyG")]')  # вкладка "Булки" на главной странице
    BREAD_SECTION_ACTIVE = (By.XPATH, './/section/div/div[1][contains(@class,"current")]')  # активная вкладка "Булки" на главной странице
    SAUCES_SECTION = (By.XPATH, './/section/div/div[2]')   # вкладка "Соусы" на главной странице
    SAUCES_SECTION_ACTIVE = (By.XPATH, './/section/div/div[2][contains(@class,"current")]')   # активная вкладка "Соусы" на главной странице
    FILLINGS_SECTION = (By.XPATH, './/section/div/div[3]')   # вкладка "Начинки" на главной странице
    FILLINGS_SECTION_ACTIVE = (By.XPATH, './/section/div/div[3][contains(@class,"current")]')   # активная вкладка "Начинки" на главной странице
