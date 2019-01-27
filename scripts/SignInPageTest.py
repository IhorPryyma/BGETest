import time
import unittest

import util.Logger as cl
import logging

from pages.HomePage import HomePage
from pages.ProfilePage import ProfilePage


class SignInPageTest(unittest.TestCase):

    log = cl.customLogger(logging.DEBUG)

    def setUp(self):
        self.homePage = HomePage()
        self.driver = self.homePage.driver
        prop = self.homePage.dic_prop
        self.signInPage = self.homePage.clickToSignIn()
        self.longMessage = False
        self.log.debug(self.id())

    def test_signInPageTitleTest(self):
        title = self.signInPage.validateSignInPageTitle()
        self.assertEqual(title, "Sign In - Udacity")

    def test_verifySignInToUdacity(self):
        profile_obj = self.signInPage.signInToUdacity()
        time.sleep(10)
        self.assertIsInstance(profile_obj, ProfilePage)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()