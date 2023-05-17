from .base_page import BasePage
from .locators import *


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert self.is_element_present(*LoginPageLocators.LOG_URL), "LOGIN_LINK is not presented"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOG_ID), "LOG_ID is not presented"
        assert self.is_element_present(*LoginPageLocators.LOG_PASS), "LOG_PASS is not presented"
        assert self.is_element_present(*LoginPageLocators.LOG_ENTER), "LOG_ENTER is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REG_MAIL), "REG_MAIL is not presented"
        assert self.is_element_present(*LoginPageLocators.REG_PASS_1), "REG_PASS_1 is not presented"
        assert self.is_element_present(*LoginPageLocators.REG_PASS_2), "REG_PASS_2 is not presented"
        assert self.is_element_present(*LoginPageLocators.REG_ENTER), "REG_ENTER is not presented"

    def register_new_user(self, email, password):
        self.browser.find_element(*LoginPageLocators.REG_MAIL).send_keys(email)
        self.browser.find_element(*LoginPageLocators.REG_PASS_1).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REG_PASS_2).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REG_ENTER).click()

