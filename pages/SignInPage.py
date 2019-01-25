from selenium.webdriver.common.by import By

from base.TestBase import TestBase
from pages.ProfilePage import ProfilePage


class SignInPage(TestBase):

    def __init__(self, dr, prop):
        # super(SignInPage, self).__init__()
        driver = dr
        self.dic_prop = prop

        self._emailTextField = driver.find_element(By.XPATH, "//input[@placeholder='Email Address']")
        self._passwordTextField = driver.find_element(By.XPATH, "//input[@placeholder='Password']")
        self._submitButton = driver.find_element(By.XPATH, "//div[@class='tabbed-pane--content--2o3OQ']//div//div//div//button[@type='button'][contains(text(),'Sign In')]")
        self._title = driver.title

    def validateSignInPageTitle(self):
        return self._title

    def signInToUdacity(self):
        self._emailTextField.send_keys(self.dic_prop.get("user_email"))
        self._passwordTextField.send_keys(self.dic_prop.get("user_password"))
        self._submitButton.click()
        return ProfilePage

    def _clearTextFields(self):
        self._emailTextField.clear()
        self._passwordTextField.clear()

