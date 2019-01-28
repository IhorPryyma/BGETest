import time
import unittest

from selenium.common.exceptions import NoSuchElementException

import util.Logger as cl
import logging

from base.EnvironmentSetup import EnvironmentSetup
from base.PageFactory import PageFactory


class SignInPageTest(EnvironmentSetup):

    log = cl.customLogger(logging.DEBUG)

    def setUp(self):
        super().setUp()
        page_obj = PageFactory()
        self.signInPage = page_obj.createPage("signin", self.driver, self.dic_prop)

    def test_verifySignInPageTitle(self):
        title = self.signInPage.validateSignInPageTitle()
        self.assertEqual(title, "Sign In - Udacity", msg="test_verifySignInPageTitle Failed")

    def test_verifyValidSignIn(self):
        self.signInPage.signInToUdacity()
        with self.assertRaises(NoSuchElementException, msg="test_verifyValidSignIn Failed"):
            time.sleep(3)
            self.screenshot.takeScreenShot(self.screenshotName)
            self.signInPage.invalidSignInMessage()

    def test_verifyInvalidSignIn(self):
        self.signInPage.setEmail(self.dic_prop.get("invalid_email", "unknown"))
        self.signInPage.setPassword(self.dic_prop.get("invalid_password", "unknown"))
        self.signInPage.clickSubmitButton()
        time.sleep(5)
        self.screenshot.takeScreenShot(self.screenshotName)
        self.assertEqual(self.signInPage.invalidSignInMessage(), "The email or password you entered is invalid",
                         msg="test_verifyInvalidSignIn Failed")


if __name__ == "__main__":
    unittest.main()
