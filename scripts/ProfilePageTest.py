import time
import unittest

import util.Logger as cl
import logging

from pages.HomePage import HomePage
from util.ScreenShot import ScreenShot


class ProfilePageTest(unittest.TestCase):

    log = cl.customLogger(logging.DEBUG)

    def setUp(self):
        self.homePage = HomePage()
        self.driver = self.homePage.driver
        prop = self.homePage.dic_prop
        self.signInPage = self.homePage.clickToSignIn()
        time.sleep(2)
        self.profilePage = self.signInPage.signInToUdacity()
        time.sleep(5)
        self.longMessage = False
        self.log.debug(self.id())

        self.screenshot = ScreenShot(self.driver)
        self.screenshotName = "./results/{}.png".format(str(self.id()).split('.')[3])


    def test_profilePageTitleTest(self):
        title = self.profilePage.validateProfileTitle()
        self.assertEqual(title, "Home - Udacity", msg="test_profilePageTitleTest Failed")

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
        self.assertEqual(self.homePage.validatHomePageTitle(), "Udacity - Free Online Classes & Nanodegrees | Udacity"
                         , msg="Something went wrong with logout!!"
                               ":: test_verifyLogout Failed")

    def tearDown(self):
        self.driver.close()
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
