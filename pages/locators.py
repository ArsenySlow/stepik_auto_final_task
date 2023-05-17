from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    MAIN_BASKET = (By.XPATH, '/html/body/header/div[1]/div/div[2]/span/a')
    EMPTY_BASKET = (By.XPATH, '/html/body/div[2]/div/div[3]/div[2]/p/a')
    EMPTY_BASKET_TEXT = (By.XPATH, '/html/body/div[2]/div/div[3]/div[2]/p/a')
    FULL_BASKET = (By.XPATH, '/html/body/div[2]/div/div[3]/div[2]/div[3]/div/div/a')
    FULL_BASKET_TEXT = (By.XPATH, '/html/body/div[2]/div/div[3]/div[2]/div[3]/div/div/a')

class LoginPageLocators:
    LOG_URL = (By.ID, 'login_link')
    LOG_ID = (By.ID, 'id_login-username')
    LOG_PASS = (By.ID, 'id_login-password')
    LOG_ENTER = (By.XPATH, '/html/body/div[2]/div/div[2]/div[2]/div/div[1]/form/button')
    REG_MAIL = (By.ID, 'id_registration-email')
    REG_PASS_1 = (By.ID, 'id_registration-password1')
    REG_PASS_2 = (By.ID, 'id_registration-password2')
    REG_ENTER = (By.XPATH, '/html/body/div[2]/div/div[2]/div[2]/div/div[2]/form/button')

class ProductPageLocators:
    ADD_TO_BUSCKET = (By.ID, 'add_to_basket_form')
    PRODUCT_NAMING = (By.CLASS_NAME, 'col-sm-6.product_main')
    BASKET_PRICE = (By.CLASS_NAME, 'alert-info')
    BASKET_ALLERT_ADDED = (By.CLASS_NAME, 'alertinner')

class BasePageLocators():
    LOGIN_LINK = (By.ID, 'login_link')
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

