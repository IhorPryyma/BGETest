from selenium.webdriver.common.by import By

from base.TestBase import TestBase
from pages.SignInPage import SignInPage
from pages.SignUpPage import SignUpPage

import util.Logger as cl
import logging


class HomePage(TestBase):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver, dict_prop):
        super(HomePage, self).__init__(driver, dict_prop)

        self.log.debug("Home page initialization")
        self._signInButton = driver.find_element(By.XPATH, "//div[@class='normal ng-star-inserted']//a[@title='Sign In'][contains(text(),'Sign In')]")
        self._signUpButton = driver.find_element(By.XPATH, "//div[@class='normal ng-star-inserted']//a[@title='Get Started'][contains(text(),'Get Started')]")
        self._title = driver.title

    def validatHomePageTitle(self):
        self.log.debug("Page title successfully found - {}".format(self._title))
        return self._title

    def getSignIn(self):
        return self._signInButton

    def getSignUp(self):
        return self._signUpButton

    def clickToSignIn(self):
        self._signInButton.click()
        self.log.debug("Sign in button verified - {}".format(str(self._signInButton)))
        self.log.debug("Loading SignInPage...")
        return SignInPage(self.driver, self.dict_prop)

    def clickToSignUp(self):
        self._signUpButton.click()
        self.log.debug("Sign un button verified - {}".format(str(self._signUpButton)))
        self.log.debug("Loading SignUpPage...")
        return SignUpPage(self.driver, self.dict_prop)
