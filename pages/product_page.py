from .base_page import BasePage
from .locators import ProductPageLocators
import math

class ProductPage(BasePage):
    def product_page_check(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_NAME), "Product name is not presented"
        assert self.is_element_present(*ProductPageLocators.PRODUCT_PRICE), "Product price is not presented"
        assert self.is_element_present(*ProductPageLocators.ADD_REWIEW_BUTTON), "Button 'Add rewiew' is not presented"
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET_BUTTON), "Button 'Add to basket' is not presented"
        assert self.is_element_present(*ProductPageLocators.INSTOCK_AVAILABILITY), "Info 'Instock availability' is not presented"

    def add_product_to_basket(self):
        add_to_busket_link = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_to_busket_link.click()
   
    def message_after_adding_check(self):
        ProductName=self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        ProductAddedMessage=self.browser.find_element(*ProductPageLocators.PRODUCT_ADDED_TO_BASKET).text
        assert ProductName == ProductAddedMessage, "Message about adding to basket ("+ProductAddedMessage+") is not equal product name ("+ProductName+")"
        ProductPrice=self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        BasketSum=self.browser.find_element(*ProductPageLocators.BASKET_SUMM_PRICE).text
        assert ProductPrice == BasketSum, "The amount of goods in the basket ("+BasketSum+") is not equal to product price ("+ProductPrice+")"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.PRODUCT_ADDED_TO_BASKET), \
           "Success message is presented, but should not be"
