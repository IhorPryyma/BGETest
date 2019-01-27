from selenium.webdriver.common.by import By

from base.TestBase import TestBase
from pages.ProfilePage import ProfilePage

import util.Logger as cl
import logging

class SignInPage(TestBase):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver, prop):
        self.log.debug("SignIn page initialization")
        self.driver = driver
        self.dic_prop = prop

        self._user = self.dic_prop.get("user_email")
        self._password = self.dic_prop.get("user_password")

        self._emailTextField = self.driver.find_element(By.XPATH, "//input[@placeholder='Email Address']")
        self._passwordTextField = self.driver.find_element(By.XPATH, "//input[@placeholder='Password']")
        self._submitButton = self.driver.find_element(By.XPATH, "//div[@class='tabbed-pane--content--2o3OQ']//div//div//div//button[@type='button'][contains(text(),'Sign In')]")
        self._title = self.driver.title

    def validateSignInPageTitle(self):
        self.log.debug("Page title successfully found - {}".format(self._title))
        return self._title

    def signInToUdacity(self):
        self._emailTextField.send_keys(self._user)
        self._passwordTextField.send_keys(self._password)
        self.log.debug("Login email: {}, password: {}".format(self._user, self._password))
        self._submitButton.click()
        return ProfilePage(self.driver, self.dic_prop)

    def _clearTextFields(self):
        self._emailTextField.clear()
        self._passwordTextField.clear()
        self.log.debug("Email and Password textfields are successfully cleared.")

