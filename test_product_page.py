import time
import pytest
from .pages.product_page import *
from .pages.basket_page import *
from .pages.login_page import *


link_main = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
link_product = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0'

@pytest.mark.add_to_basket
class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self,browser):
        self.link = 'http://selenium1py.pythonanywhere.com/ru/'
        page = LoginPage(browser,self.link)
        page.open()  # открываем страницу
        page.go_to_login_page()
        email = str(time.time()) + "@fakemail.org"
        password = 'aezakmihesoyam'
        page.register_new_user(email,password)
        page.should_be_authorized_user()


    def test_guest_cant_see_success_message(self, browser):
        page = ProductPage(browser, link_product)
        page.open()  # открываем страницу
        page.should_not_be_success_message()

    def test_guest_can_add_product_to_basket(self,browser):
        page = ProductPage(browser, link_product)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
        page.open()                      # открываем страницу
        page.adding_products()
        page.should_be_added_product()



# @pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
#                                   pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", marks=pytest.mark.xfail),
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
# def test_guest_can_add_product_to_basket(browser):
#     link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0'
#     page = ProductPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
#     page.open()                      # открываем страницу
#     page.adding_products()
#     page.should_be_added_product()

 # def test_guest_cant_see_success_message(browser):
 #     page = ProductPage(browser, link_product)
 #     page.open()  # открываем страницу
 #     page.should_not_be_success_message()



# def test_guest_should_see_login_link_on_product_page(browser):
#     page = ProductPage(browser, link_main)
#     page.open()
#     # page.go_to_login_page()
#     page.should_be_login_link()
#
# def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
#     page = BasePage(browser, link_product)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
#     page.open()
#     page.go_to_basket()
#     page = BasketPage(browser, link_product)
#     page.should_not_be_added_to_basket()
#     page.should_not_be_text_of_adding_to_basket()

# def test_guest_can_go_to_login_page_from_product_page(browser):
#     page = ProductPage(browser, link_main)
#     page.open()
#     page.should_be_login_link()
#
# @pytest.mark.xfail(reason="fixing this bug right now")
# def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
#     page = ProductPage(browser,link_product)
#     page.open()  # открываем страницу
#     page.adding_products()
#     page.should_not_be_success_message()
#

#
# @pytest.mark.xfail(reason="fixing this bug right now")
# def test_message_disappeared_after_adding_product_to_basket(browser):
#     page = ProductPage(browser,link_product)
#     page.open()  # открываем страницу
#     page.adding_products()
#     page.should_dissapear_of_success_message()