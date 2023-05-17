from .base_page import BasePage
from .locators import *

class BasketPage(BasePage):

    def should_not_be_added_to_basket(self):
        assert self.is_element_present(*MainPageLocators.EMPTY_BASKET)

    def should_not_be_text_of_adding_to_basket (self):
        assert self.is_element_present(*MainPageLocators.EMPTY_BASKET_TEXT), "Success message is presented, but should not be"

    def should_be_added_to_basket(self):
        assert self.is_not_element_present(*MainPageLocators.FULL_BASKET)

    def should_be_text_of_adding_to_basket (self):
        assert self.is_not_element_present(*MainPageLocators.FULL_BASKET_TEXT), "Success message is presented, but should not be"


languages = {
    "ar": "سلة التسوق فارغة",
    "ca": "La seva cistella està buida.",
    "cs": "Váš košík je prázdný.",
    "da": "Din indkøbskurv er tom.",
    "de": "Ihr Warenkorb ist leer.",
    "en": "Your basket is empty.",
    "el": "Το καλάθι σας είναι άδειο.",
    "es": "Tu carrito esta vacío.",
    "fi": "Korisi on tyhjä",
    "fr": "Votre panier est vide.",
    "it": "Il tuo carrello è vuoto.",
    "ko": "장바구니가 비었습니다.",
    "nl": "Je winkelmand is leeg",
    "pl": "Twój koszyk jest pusty.",
    "pt": "O carrinho está vazio.",
    "pt-br": "Sua cesta está vazia.",
    "ro": "Cosul tau este gol.",
    "ru": "Ваша корзина пуста",
    "sk": "Váš košík je prázdny",
    "uk": "Ваш кошик пустий.",
    "zh-cn": "Your basket is empty.",
}