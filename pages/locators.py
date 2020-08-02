from selenium.webdriver.common.by import By

class MainPageLocators():
    # login link:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPagesLocators():

    # login form:
    ID_LOGIN_USERNAME = (By.CSS_SELECTOR, "#id_login-username")
    ID_LOGIN_PASSWORD = (By.CSS_SELECTOR, "#id_login-password")

    # registration form:
    ID_REGISTRATION_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    ID_REGISTRATION_PASSWORD1 = (By.CSS_SELECTOR, "#id_registration-password1")
    ID_REGISTRATION_PASSWORD2 = (By.CSS_SELECTOR, "#id_registration-password2")