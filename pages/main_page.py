from .base_page import BasePage
from .locators import MainPageLocators
from .login_page import LoginPage
import time

class MainPage(BasePage):

    def go_to_login_page(self):
        #login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        #login_link.click()
        link = self.browser.find_element_by_css_selector("#login_link")
        link.click()
        #time.sleep(10)
        #alert = self.browser.switch_to.alert
        #alert.accept()
        #return LoginPage(browser=self.browser, url=self.browser.current_url)

    def should_be_login_link(self):
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented"



