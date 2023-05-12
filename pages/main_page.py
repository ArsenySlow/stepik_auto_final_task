from .base_page import BasePage
from .locators import MainPageLocators
from .locators import LoginPageLocators


class MainPage(BasePage):
    def go_to_login_page(self):
        login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        login_link.click()

    def should_be_login_url(self):
        self.browser.find_element(*MainPageLocators.LOGIN_LINK)

    def should_be_login_page(self):
        self.browser.find_element(*LoginPageLocators.LOG_URL)

    def should_be_login_form(self):
        self.browser.find_element(*LoginPageLocators.LOG_ID)
        self.browser.find_element(*LoginPageLocators.LOG_PASS)
        self.browser.find_element(*LoginPageLocators.LOG_ENTER)

    def should_be_register_form(self):
        self.browser.find_element(*LoginPageLocators.REG_MAIL)
        self.browser.find_element(*LoginPageLocators.REG_PASS_1)
        self.browser.find_element(*LoginPageLocators.REG_PASS_2)
        self.browser.find_element(*LoginPageLocators.REG_ENTER)
