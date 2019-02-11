
from selenium.webdriver.support.abstract_event_listener import  AbstractEventListener

import util.Logger as cl
import logging

from util.ScreenShot import ScreenShot


class WebEventListener(AbstractEventListener):

    log = cl.customLogger(logging.DEBUG)

    def before_navigate_to(self, url, driver):
        self.log.debug("Before navigating to: '" + str(url) + "'")

    def after_navigate_to(self, url, driver):
        self.log.debug("Navigated to:'" + str(url) + "'")

    def before_navigate_back(self, driver):
        self.log.debug("Navigating back to previous page")

    def after_navigate_back(self, driver):
        self.log.debug("Navigated back to previous page")

    def before_navigate_forward(self, driver):
        self.log.debug("Navigating forward to next page")

    def after_navigate_forward(self, driver):
        self.log.debug("Navigated forward to next page")

    def before_find(self, by, value, driver):
        self.log.debug("Trying to find Element By : " + str(by) + " value: " + str(value))

    def after_find(self, by, value, driver):
        self.log.debug("Found Element By : " + str(by) + " value: " + str(value))

    def before_click(self, element, driver):
        self.log.debug("Trying to click on: " + str(element))

    def after_click(self, element, driver):
        self.log.debug("Clicked on: " + str(element))

    def before_change_value_of(self, element, driver):
        self.log.debug("Value of the:" + str(element) + " before any changes made")

    def after_change_value_of(self, element, driver):
        self.log.debug("Element value changed to: " + str(element))

    def before_execute_script(self, script, driver):    pass

    def after_execute_script(self, script, driver): pass

    def before_close(self, driver):
        self.log.debug("Trying to close the browser")

    def after_close(self, driver):
        self.log.debug("Browser was closed")

    def before_quit(self, driver):
        self.log.debug("Trying to quit the browser")

    def after_quit(self, driver):
        self.log.debug("Test was quited")

    def on_exception(self, exception, driver):
        self.log.error("!!! " + str(exception))
