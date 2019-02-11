import unittest

from properties.p import Property
from selenium import webdriver

from selenium.webdriver.support.event_firing_webdriver import EventFiringWebDriver


import util.Logger as cl
import logging

from util.ScreenShot import ScreenShot
from util.WebEventListener import WebEventListener


class EnvironmentSetup(unittest.TestCase):

    PAGE_LOAD_TIME = 20
    IMPLICITLY_WAIT = 10

    log = cl.customLogger(logging.DEBUG)

    def setUp(self):

        self.log.debug("Properties initialization")
        self.prop = Property()
        try:
            self.dic_prop = self.prop.load_property_files("/Users/user/PycharmProjects/BGETest/config/config.properties")
            self.log.debug("Properties successfully loaded.")
            self.log.debug(self.dic_prop)
        except FileNotFoundError as err:
            self.log.error("config.properties file not found!!!")
            raise ValueError("There is no config.properties file in the project directory" + str(err))

        browserName = self.dic_prop.get("browser", "chrome")

        if browserName.lower() == "firefox":
            self.driver = webdriver.Firefox()
            self.log.debug("Object for firefox is created - " + str(self.driver))
        elif browserName.lower() == "chrome":
            self.driver = webdriver.Chrome()
            self.log.debug("Object for chrome is created - " + str(self.driver))
        elif browserName.lower() == "safari":
            self.driver = webdriver.Safari()
            self.log.debug("Object for safari is created - " + str(self.driver))
        else:
            raise ValueError("Unknown browser, please check the config.properties file")

        self.eventListener = WebEventListener()
        self.driver = EventFiringWebDriver(self.driver, self.eventListener)

        self.driver.maximize_window()
        self.driver.delete_all_cookies()
        self.log.debug("Cookies are successfully deleted")

        self.driver.set_page_load_timeout(self.PAGE_LOAD_TIME)
        self.driver.implicitly_wait(self.IMPLICITLY_WAIT)
        self.driver.get(self.dic_prop.get("url"))

        self.longMessage = False
        self.log.debug(self.id())

        self.screenshot = ScreenShot(self.driver)

        try:
            self.screenshotName = "./results/{}.png".format(str(self.id()).split('.')[3])
        except IndexError:
            self.screenshotName = "./results/{}.png".format(str(self.id()).split('.')[2])

    def tearDown(self):
        if self.driver is not None:
            self.driver.close()
            self.driver.quit()
