from selenium.webdriver.common.by import By

from base.TestBase import TestBase
from pages.HomePage import HomePage


class ProfilePage(TestBase):

    def __init__(self, driver, prop):
        self.log.debug("Profile page initialization")

        self.driver = driver
        self.dic_prop = prop

        self._home = self.driver.find_element(By.XPATH, "//a[@title='Home']")
        self._catalog = self.driver.find_element(By.XPATH, "//a[@title='Catalog']")
        self._settings = self.driver.find_element(By.XPATH, "//a[@title='Settings']")
        self._logoutButton = self.driver.find_element(By.XPATH, "//a[@title='Logout']")
        self._title = self.driver.title

    def validateProfileTitle(self):
        self.log.debug("Page title successfully found - {}".format(self._title))
        return self._title

    def validateHomeLink(self):
        return self._home.isdisplayed()

    def validateCatalogLink(self):
        return self._catalog.isdisplayed()

    def validateSettingsLink(self):
        return self._logoutButton.isdisplayed()

    def validateLogout(self):
        self._logoutButton.click()
        self.log.debug("Loading home page...")
        return HomePage()
