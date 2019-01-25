from selenium.webdriver.common.by import By

from base.TestBase import TestBase
from pages.ProfilePage import ProfilePage
from util.UserGenerator import UserGenerator


class SignUpPage(TestBase):

    def __init__(self, dr, prop):
        # super(SignInPage, self).__init__()
        driver = dr
        self.dic_prop = prop
        self._newUser = UserGenerator()

        self._firstName = driver.find_element(By.XPATH, "//input[@placeholder='First Name']")
        self._lastName = driver.find_element(By.XPATH, "//input[@placeholder='Last Name']")
        self._email = driver.find_element(By.XPATH, "//input[@placeholder='Email Address']")
        self._password = driver.find_element(By.XPATH, "//input[@placeholder='Password']")
        self._confirmPassword = driver.find_element(By.XPATH, "//input[@placeholder='Confirm Password']")
        self._signUpButton = driver.find_element(By.XPATH, "//div[@class='tabbed-pane--content--2o3OQ']//div//div//div//button[@type='button'][contains(text(),'Sign Up')]")
        self._title = driver.title

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
        return ProfilePage

    def _clearTextFields(self):
        self._firstName.clear()
        self._lastName.clear()
        self._email.clear()
        self._password.clear()
        self._confirmPassword.clear()
