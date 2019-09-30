from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")

class ProductPageLocators():
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    ADD_REWIEW_BUTTON = (By.CSS_SELECTOR, "#write_review")
    INSTOCK_AVAILABILITY = (By.CSS_SELECTOR, ".product_main > p.instock.availability")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main > h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "p.price_color")
    ADDED_TO_BASKET_MESSAGE = (By.CSS_SELECTOR, "#messages > div:nth-child(1) > div")
    PRODUCT_ADDED_TO_BASKET = (By.CSS_SELECTOR, "#messages > div:nth-child(1) > div > strong")
    BASKET_SUMM_MESSAGE = (By.CSS_SELECTOR, ".alert-info.fade.in > div")
    BASKET_SUMM_PRICE = (By.CSS_SELECTOR, ".alert-info.fade.in > div > p:nth-child(1) > strong")
    GO_TO_BASKET_BUTTON = (By.CSS_SELECTOR, ".alert-info.fade.in > div > p:nth-child(2) > a:nth-child(1)")
    GO_TO_CHECKOUT = (By.CSS_SELECTOR, ".alert-noicon.alert-info.fade.in > div > p:nth-child(2) > a:nth-child(2)")
