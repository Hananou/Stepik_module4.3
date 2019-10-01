from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):

    def basket_should_be_empty(self):
        assert self.is_not_element_present(*BasketPageLocators.ITEMS_TO_BY_LIST), \
           "Items in the basket is presented, but should not be"

    def basket_is_empty_message_presented(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET_MESSAGE), "'Basket is empty' message is not presented"
        BasketIsEmptyMessage = self.browser.find_element(*BasketPageLocators.EMPTY_BASKET_MESSAGE).text
        assert len('BasketIsEmptyMessage') > 0 , "'Basket is empty' message does not contain text"


