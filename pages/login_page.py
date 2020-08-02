from .base_page import BasePage
from .locators import LoginPagesLocators

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert "login" in self.browser.current_url, "Word \"login\" not in current url"

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPagesLocators.ID_LOGIN_USERNAME), "Login from is not presented"
        assert self.is_element_present(*LoginPagesLocators.ID_LOGIN_PASSWORD), "Password from is not presented"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPagesLocators.ID_REGISTRATION_EMAIL), "Login from is not presented"
        assert self.is_element_present(*LoginPagesLocators.ID_REGISTRATION_PASSWORD1), "Password from is not presented"
        assert self.is_element_present(*LoginPagesLocators.ID_REGISTRATION_PASSWORD2), "Confirm Password from is not presented"