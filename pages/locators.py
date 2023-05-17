from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOG_URL = (By.ID, 'login_link')
    LOG_ID = (By.ID, 'id_login-username')
    LOG_PASS = (By.ID, 'id_login-password')
    LOG_ENTER = (By.XPATH, '/html/body/div[2]/div/div[2]/div[2]/div/div[1]/form/button')
    REG_MAIL = (By.ID, 'id_registration-email')
    REG_PASS_1 = (By.ID, 'id_registration-password1')
    REG_PASS_2 = (By.ID, 'id_registration-password2')
    REG_ENTER = (By.XPATH, '/html/body/div[2]/div/div[2]/div[2]/div/div[2]/form/button')
