import time
import util.Logger as cl
import logging

from selenium.webdriver.common.by import By

from base.TestBase import TestBase


class ProfilePage(TestBase):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver, dict_prop):
        super(ProfilePage, self).__init__(driver, dict_prop)
        self.log.debug("Profile page initialization")
        time.sleep(2)
        self._home = self.driver.find_element(By.XPATH, "//a[@title='Home']")
        self._catalog = self.driver.find_element(By.XPATH, "//a[@title='Catalog']")
        self._settings = self.driver.find_element(By.XPATH, "//a[@title='Settings']")
        self._logoutButton = self.driver.find_element(By.XPATH, "//a[@title='Logout']")
        self._homeHeader = self.driver.find_element(By.XPATH, "//div[@class='_layout-module--title-area--1yynf']//div[@class='_header-module--header--1boX-']//div//h1[@aria-live='assertive'][contains(text(),'Home')]")
        time.sleep(2)
        self._title = self.driver.title

    def validateProfilePageTitle(self):
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

    def clickCatalog(self):
        self._catalog.click()

    def clickSettings(self):
        self._settings.click()

    def getHomeHeader(self):
        return self._homeHeader

