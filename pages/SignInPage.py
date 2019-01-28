from selenium.webdriver.common.by import By

from base.TestBase import TestBase
from pages.ProfilePage import ProfilePage

import util.Logger as cl
import logging


class SignInPage(TestBase):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver, dict_prop):
        super(SignInPage, self).__init__(driver, dict_prop)
        self.log.debug("SignIn page initialization")

        self._user = dict_prop.get("user_email")
        self._password = dict_prop.get("user_password")

        self._emailTextField = driver.find_element(By.XPATH, "//input[@placeholder='Email Address']")
        self._passwordTextField = driver.find_element(By.XPATH, "//input[@placeholder='Password']")
        self._submitButton = driver.find_element(By.XPATH, "//div[@class='tabbed-pane--content--2o3OQ']//div//div//div//button[@type='button'][contains(text(),'Sign In')]")
        self._title = driver.title

    def validateSignInPageTitle(self):
        self.log.debug("Page title successfully found - {}".format(self._title))
        return self._title

    def setEmail(self, email):
        self._emailTextField.send_keys(email)

    def setPassword(self, password):
        self._passwordTextField.send_keys(password)

    def clickSubmitButton(self):
        self._submitButton.click()

    def invalidSignInMessage(self):
        return self.driver.find_element(By.XPATH, "//div[contains(@class,'alert--error--3iAkS alert--_alert--1gt-I')]").text

    def signInToUdacity(self):
        self._emailTextField.send_keys(self._user)
        self._passwordTextField.send_keys(self._password)
        self.log.debug("Login email: {}, password: {}".format(self._user, self._password))
        self._submitButton.click()
        return ProfilePage(self.driver, self.dict_prop)

    def _clearTextFields(self):
        self._emailTextField.clear()
        self._passwordTextField.clear()
        self.log.debug("Email and Password textfields are successfully cleared.")
