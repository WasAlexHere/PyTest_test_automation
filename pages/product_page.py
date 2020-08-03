from .base_page import BasePage
from .locators import ItemPagesLocators

class ProductPage(BasePage):

    def should_be_add_to_basket_button(self):
        assert self.is_element_present(*ItemPagesLocators.ADD_TO_BASKET_BUTTON), "Add to basket button is not presented"
        self.add_to_basket_button = self.browser.find_element_by_xpath("//*[@id='add_to_basket_form']/button")
        self.add_to_basket_button.click()

    def item_should_be_added_to_basket(self):
        self.item = self.browser.find_element_by_xpath("//*[@id='content_inner']/article/div[1]/div[2]/h1")
        self.item_text = self.item.text
        print("%a was added to basket!" % self.item_text)

    def count_price_of_basket(self):
        self.price_of_the_basket = self.browser.find_element_by_xpath("//*[@id='content_inner']/article/div[1]/div[2]/p[1]")
        self.price_of_the_basket_text = self.price_of_the_basket.text
        print("The Current price of your basket is: ", self.price_of_the_basket_text)