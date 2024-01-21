from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#registration_link")


class LoginPageLocators:
    REGISTRATION_FORM = (By.CSS_SELECTOR, "#register_form")
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")


class ProductPageLocators:
    ADD_TO_CART = (By.CSS_SELECTOR, ".btn.btn-lg.btn-primary.btn-add-to-basket")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "p.price_color")
    SUM_PRICE = (By.XPATH, "//*[@id='messages']/div[3]/div/p[1]/strong")
    NAME_OF_PRODUCT_AFTER_ADD_TO_CART = (By.XPATH, "//*[@id='messages']/div[1]/div/strong")
    NAME_OF_PRODUCT_BEFORE_ADD_TO_CART = (By.CSS_SELECTOR, ".col-sm-6.product_main h1")
