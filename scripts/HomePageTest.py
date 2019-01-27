import unittest

import util.Logger as cl
import logging

from pages.SignUpPage import SignUpPage
from pages.HomePage import HomePage
from pages.SignInPage import SignInPage
from util.ScreenShot import ScreenShot


class HomePageTest(unittest.TestCase):

    log = cl.customLogger(logging.DEBUG)

    def setUp(self):

        self.homePage = HomePage()
        self.driver = self.homePage.driver
        self.longMessage = False
        self.log.debug(self.id())

        self.screenshot = ScreenShot(self.driver)
        try:
            self.screenshotName = "./results/{}.png".format(str(self.id()).split('.')[3])
        except Exception:
            self.screenshotName = "./results/{}.png".format(str(self.id()).split('.')[2])


    def test_homePageTitleTest(self):
        title = self.homePage.validatHomePageTitle()
        self.assertEqual(title, "Udacity - Free Online Classes & Nanodegrees | Udacity", msg="test_homePageTitleTest Failed")

    def test_verifySignInButton(self):
        login_obj = self.homePage.clickToSignIn()
        self.screenshot.takeScreenShot(self.screenshotName)
        self.assertIsInstance(login_obj, SignInPage, msg="test_validateSignInButton Failed")

    def test_verifySignUpButton(self):
        register_obj = self.homePage.clickToSignUp()
        self.screenshot.takeScreenShot(self.screenshotName)
        self.assertIsInstance(register_obj, SignUpPage, msg="test_validateSignUpButton Failed")

    def tearDown(self):
        self.driver.close()
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
