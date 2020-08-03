from .base_page import BasePage
from .locators import ItemPagesLocators

class ProductPage(BasePage):

    def should_be_add_to_basket_button(self):
        assert self.is_element_present(*ItemPagesLocators.ADD_TO_BASKET_BUTTON), "Add to basket button is not presented"
        self.add_to_basket_button = self.browser.find_element_by_xpath("//*[@id='add_to_basket_form']/button")
        self.add_to_basket_button.click()