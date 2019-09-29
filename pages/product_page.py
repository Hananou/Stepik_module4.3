from .base_page import BasePage
from .locators import ProductPageLocators
import math

class ProductPage(BasePage):
    def add_product_to_basket(self):
        add_to_busket_link = self.browser.find_element(*ProductPageLocators.PRODUCT_LINK)
        add_to_busket_link.click()
