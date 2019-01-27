from selenium.webdriver.common.by import By

from base.TestBase import TestBase
from pages.ProfilePage import ProfilePage
from util.UserGenerator import UserGenerator

import util.Logger as cl
import logging


class SignUpPage(TestBase):

    log = cl.customLogger(logging.DEBUG)


    def __init__(self, driver, prop):
        self.log.debug("SignUp page initialization")
        self.driver = driver
        self.dic_prop = prop
        self._newUser = UserGenerator()

        self._firstName = self.driver.find_element(By.XPATH, "//input[@placeholder='First Name']")
        self._lastName = self.driver.find_element(By.XPATH, "//input[@placeholder='Last Name']")
        self._email = self.driver.find_element(By.XPATH, "//input[@placeholder='Email Address']")
        self._password = self.driver.find_element(By.XPATH, "//input[@placeholder='Password']")
        self._confirmPassword = self.driver.find_element(By.XPATH, "//input[@placeholder='Confirm Password']")
        self._signUpButton = self.driver.find_element(By.XPATH, "//div[@class='tabbed-pane--content--2o3OQ']//div//div//div//button[@type='button'][contains(text(),'Sign Up')]")
        self._title = self.driver.title

    def validateSignUpPageTitle(self):
        self.log.debug("Page title successfully found - {}".format(self._title))
        return self._title

    def signUpToUdacity(self):
        self._clearTextFields()
        self._firstName.send_keys(self._newUser.generateName())
        self._lastName.send_keys(self._newUser.generateName())
        self._email.send_keys(self._newUser.generateEmail())
        self._password.send_keys(self._newUser.generatrPassword())
        self._confirmPassword.send_keys(self._newUser.generatrPassword())
        self._signUpButton.click()
        self.log.debug("Loading Profile page...")
        return ProfilePage(self.driver, self.dic_prop)

    def _clearTextFields(self):
        self._firstName.clear()
        self._lastName.clear()
        self._email.clear()
        self._password.clear()
        self._confirmPassword.clear()
        self.log.debug("Registration textfields are successfully cleared.")
