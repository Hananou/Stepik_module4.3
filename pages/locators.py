from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_BUTTON = (By.CSS_SELECTOR, "div.basket-mini.pull-right.hidden-xs > span > a")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class BasketPageLocators():
    EMPTY_BASKET_MESSAGE = (By.CSS_SELECTOR, "#content_inner > p")
    ITEMS_TO_BY_LIST = (By.CSS_SELECTOR, ".col-sm-6.h3")

class LoginPageLocators():
#login_form
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    LOGIN_USERNAME = (By.CSS_SELECTOR, "#id_login-username")
    LOGIN_PASSWORD = (By.CSS_SELECTOR, "#id_login-password")
    PASSWORD_RESET = (By.CSS_SELECTOR, "#login_form > p > a")
    LOGIN_SUBMIT = (By.CSS_SELECTOR, "#login_form > button")
#register_form
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    REGISTRATION_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTRATION_PASSWORD1 = (By.CSS_SELECTOR, "#id_registration-password1")
    REGISTRATION_PASSWORD2 = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTRATION_SUBMIT = (By.CSS_SELECTOR, "#register_form > button")

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
    GO_TO_CHECKOUT = (By.CSS_SELECTOR, ".in > div > p:nth-child(2) > a:nth-child(2)")



