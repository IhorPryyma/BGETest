from selenium.webdriver.common.by import By

from base.TestBase import TestBase
from pages.ProfilePage import ProfilePage
from util.UserGenerator import UserGenerator


class SignUpPage(TestBase):

    def __init__(self, driver, prop):
        # super(SignInPage, self).__init__()
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
        return self._title

    def signUpToUdacity(self):
        self._clearTextFields()
        self._firstName.send_keys(self._newUser.generateName())
        self._lastName.send_keys(self._newUser.generateName())
        self._email.send_keys(self._newUser.generateEmail())
        self._password.send_keys(self._newUser.generatrPassword())
        self._confirmPassword.send_keys(self._newUser.generatrPassword())
        self._signUpButton.click()
        return ProfilePage(self.driver, self.dic_prop)

    def _clearTextFields(self):
        self._firstName.clear()
        self._lastName.clear()
        self._email.clear()
        self._password.clear()
        self._confirmPassword.clear()
