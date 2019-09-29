from .base_page import BasePage
from .locators import ProductPageLocators
import math

class ProductPage(BasePage):
    def add_product_to_basket(self):
        add_to_busket_link = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_to_busket_link.click()
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET_BUTTON), "Button 'Add to basket' is not presented"
        assert self.is_element_present(*ProductPageLocators.ADD_REWIEW_BUTTON), "Button 'Add rewiew' is not presented"
        assert self.is_element_present(*ProductPageLocators.INSTOCK_AVAILABILITY), "Info 'Instock availability' is not presented"
        assert PRODUCT_NAME in PRODUCT_ADDED_TO_BASKET, "Message about adding to basket ("+PRODUCT_ADDED_TO_BASKET+") does not contain product name ("+PRODUCT_NAME+")"