from .base_page import BasePage
from .locators import LoginPageLocators

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()
    def should_be_login_url(self):
        assert 'login' in self.browser.current_url, "Page addres does not contain text 'login': "+self.browser.current_url
    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"
        assert self.is_element_present(*LoginPageLocators.LOGIN_USERNAME), "Username field is not presented"
        assert self.is_element_present(*LoginPageLocators.LOGIN_PASSWORD), "Password field is not presented"
        assert self.is_element_present(*LoginPageLocators.PASSWORD_RESET), "Password reset link is not presented"
        assert self.is_element_present(*LoginPageLocators.LOGIN_SUBMIT), "Login submit button is not presented"
    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_EMAIL), "Registration email field is not presented"
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_PASSWORD1), "Registration password1 field is not presented"
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_PASSWORD2), "Registration password2 field is not presented"
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_SUBMIT), "Registration submit button is not presented"
