import time
import pytest
from .pages.product_page import *
from .pages.basket_page import *
from .pages.login_page import *


link_product = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0'

@pytest.mark.add_to_basket
class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self,browser):
        self.link = 'http://selenium1py.pythonanywhere.com/ru/'
        page = LoginPage(browser,self.link)
        page.open()  # открываем страницу
        page.go_to_login_page()  # переходим к старнице авторизации
        email = str(time.time()) + "@fakemail.org"
        password = 'aezakmihesoyam'
        page.register_new_user(email,password) # вводим сгенерированные данные
        page.should_be_authorized_user() # проверка, что пользователь авторизован

    def test_user_cant_see_success_message(self, browser):
        page = ProductPage(browser, link_product)
        page.open()  # открываем страницу
        page.should_not_be_success_message()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self,browser):
        page = ProductPage(browser, link_product)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
        page.open()                      # открываем страницу продукта
        page.adding_products()           # Добавляем продукт в корзину
        page.should_be_added_product()   # Проверка, что продукт был добавлен в корзину корректно


@pytest.mark.need_review
@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                  pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", marks=pytest.mark.xfail),
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
def test_guest_can_add_product_to_basket(browser,link):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0'
    page = ProductPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()                         # открываем страницу
    page.adding_products()              # добавляем продукт в корзину
    page.should_be_added_product()      # проверяем, что продукт добавлен в корзину корректно


def test_guest_should_see_login_link_on_product_page(browser):
    page = ProductPage(browser, link_product)
    page.open()
    page.should_be_login_link()

@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    page = BasePage(browser, link_product)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()                             # открываем страницу
    page.go_to_basket()                     # переходим в корзину
    page = BasketPage(browser, link_product)
    page.should_not_be_added_to_basket()    # проверяем, что продукт добавлен
    page.should_not_be_text_of_adding_to_basket() # проверяем, что тект о добавлении продукта отображается

@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    page = ProductPage(browser, link_product)
    page.open()                             # открываем страницу
    page.go_to_login_page()                 # переходим на страницу авторизации
    page.should_be_login_link()             # проверка, что страница авторизации действительна

@pytest.mark.xfail(reason="fixing this bug right now")
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = ProductPage(browser,link_product)
    page.open()  # открываем страницу
    page.adding_products()
    page.should_not_be_success_message()

def test_guest_cant_see_success_message(browser):
     page = ProductPage(browser, link_product)
     page.open()  # открываем страницу
     page.should_not_be_success_message()

@pytest.mark.xfail(reason="fixing this bug right now")
def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser,link_product)
    page.open()  # открываем страницу
    page.adding_products()
    page.should_dissapear_of_success_message()