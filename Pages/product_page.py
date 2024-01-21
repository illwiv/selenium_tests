from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def should_be_add_to_cart(self):
        add_to_cart_button = self.browser.find_element(*ProductPageLocators.ADD_TO_CART)
        add_to_cart_button.click()
        self.solve_quiz_and_get_code()
        assert self.check_equal_values(*ProductPageLocators.PRODUCT_PRICE,
                                      *ProductPageLocators.SUM_PRICE), f"{self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text} not equal {self.browser.find_element(*ProductPageLocators.SUM_PRICE).text}"
        assert self.check_equal_values(*ProductPageLocators.NAME_OF_PRODUCT_AFTER_ADD_TO_CART,
                                      *ProductPageLocators.NAME_OF_PRODUCT_BEFORE_ADD_TO_CART), f"{self.browser.find_element(*ProductPageLocators.NAME_OF_PRODUCT_BEFORE_ADD_TO_CART).text} not equal {self.browser.find_element(*ProductPageLocators.NAME_OF_PRODUCT_AFTER_ADD_TO_CART).text}"
