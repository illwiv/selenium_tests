from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        assert self.should_be_login_url(), f"'/login' not in {self.browser.current_url}"
        assert self.should_be_login_form(*LoginPageLocators.LOGIN_FORM), f'No such element {LoginPageLocators.LOGIN_FORM[1]}'
        assert self.should_be_register_form(
            *LoginPageLocators.REGISTRATION_FORM), f'No such element {LoginPageLocators.REGISTRATION_FORM[1]}'
