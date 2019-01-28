import time
import unittest

from selenium.common.exceptions import StaleElementReferenceException

import util.Logger as cl
import logging

from base.EnvironmentSetup import EnvironmentSetup
from base.PageFactory import PageFactory


class ProfilePageTest(EnvironmentSetup):

    log = cl.customLogger(logging.DEBUG)

    def setUp(self):
        super().setUp()
        page_obj = PageFactory()
        self.profilePage = page_obj.createPage("profile", self.driver, self.dic_prop)

    def test_verifyProfilePageTitle(self):
        title = self.profilePage.validateProfilePageTitle()
        self.assertEqual(title, "Home - Udacity", msg="test_verifyProfilePageTitle Failed")

    def test_verifyElementsOfProfilePage(self):
        self.screenshot.takeScreenShot(self.screenshotName)

        self.assertTrue(self.profilePage.validateHomeLink(), msg="test_verifyElementsOfProfilePage Failed "
                                                                 ":: Home link not found")
        self.assertTrue(self.profilePage.validateCatalogLink(), msg="test_verifyElementsOfProfilePage Failed "
                                                                    ":: Catalog link not found")
        self.assertTrue(self.profilePage.validateSettingsLink(), msg="test_verifyElementsOfProfilePage Failed "
                                                                     ":: Settings link not found")

    def test_verifyLogout(self):
        self.profilePage.validateLogout()
        self.screenshot.takeScreenShot(self.screenshotName)
        time.sleep(2)
        with self.assertRaises(StaleElementReferenceException):
            self.profilePage.getHomeHeader().is_displayed()


if __name__ == "__main__":
    unittest.main()
