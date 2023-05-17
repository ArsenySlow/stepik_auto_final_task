from .base_page import BasePage
from .login_page import LoginPage
from .locators import MainPageLocators


class MainPage(BasePage):
    def go_to_login_page(self):
        login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        login_link.click()

        # return LoginPage(browser=self.browser, url=self.browser.current_url)
        # alert = self.browser.switch_to.alert      #ЕСЛИ ЕСТЬ АЛЕРТ
        # alert.accept()

    def should_be_login_url(self):
        self.browser.find_element(*MainPageLocators.LOGIN_LINK)

