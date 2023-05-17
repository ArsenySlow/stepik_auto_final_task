from .base_page import *
from .locators import *


class ProductPage(BasePage):

    def adding_products(self):
        self.browser.find_element(*ProductPageLocators.ADD_TO_BUSCKET).click()
        self.solve_quiz_and_get_code()

    def should_be_added_product(self):
        self.should_be_correct_name_added()
        self.should_be_correct_price()

    def should_be_correct_name_added(self):
        name_correct = self.browser.find_element(*ProductPageLocators.PRODUCT_NAMING).text
        name_correct = name_correct.split("£")[0].split('\n')[0]
        text_notification = self.browser.find_element(*ProductPageLocators.BASKET_ALLERT_ADDED).text
        assert f'{name_correct} has been added to your basket.' == text_notification

    def should_be_correct_price(self):
        price_correct = self.browser.find_element(*ProductPageLocators.PRODUCT_NAMING).text
        price_correct = price_correct.split("£")[1].split('\n')[0]
        price_basket = self.browser.find_element(*ProductPageLocators.BASKET_PRICE).text
        price_basket = price_basket.split("£")[1].split('\n')[0]
        assert price_basket == price_correct


    def should_not_be_success_message(self):

        assert self.is_not_element_present(*ProductPageLocators.BASKET_PRICE), "Success message is presented, but should not be"

    def should_dissapear_of_success_message (self):
        assert self.is_disappeared(*ProductPageLocators.BASKET_PRICE), "Success message is presented, but should not be"

