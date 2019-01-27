import time
import util.Logger as cl
import logging

from selenium.webdriver.common.by import By

from base.TestBase import TestBase


class ProfilePage(TestBase):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver, prop):
        self.log.debug("Profile page initialization")

        self.driver = driver
        self.dic_prop = prop
        time.sleep(5)
        self._home = self.driver.find_element(By.XPATH, "//a[@title='Home']")
        self._catalog = self.driver.find_element(By.XPATH, "//a[@title='Catalog']")
        self._settings = self.driver.find_element(By.XPATH, "//a[@title='Settings']")
        self._logoutButton = self.driver.find_element(By.XPATH, "//a[@title='Logout']")
        time.sleep(2)
        self._title = self.driver.title

    def validateProfileTitle(self):
        self.log.debug("Page title successfully found - {}".format(self._title))
        return self._title

    def validateHomeLink(self):
        return self._home.is_displayed()

    def validateCatalogLink(self):
        return self._catalog.is_displayed()

    def validateSettingsLink(self):
        return self._settings.is_displayed()

    def validateLogout(self):
        self._logoutButton.click()
        self.log.debug("Loading home page...")

