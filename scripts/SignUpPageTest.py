import time
import unittest

from selenium.common.exceptions import NoSuchElementException

import util.Logger as cl
import logging

from base.EnvironmentSetup import EnvironmentSetup
from base.PageFactory import PageFactory


class SignUpPageTest(EnvironmentSetup):

    log = cl.customLogger(logging.DEBUG)

    def setUp(self):
        super().setUp()
        page_obj = PageFactory()
        self.signUpPage = page_obj.createPage("signup", self.driver, self.dic_prop)

    def test_verifySignUpPageTitle(self):
        title = self.signUpPage.validateSignUpPageTitle()
        self.assertEqual(title, "Sign Up - Udacity", msg="test_verifySignUpPageTitle Failed")

    def test_verifyValidSignUp(self):
        self.signUpPage.signUpToUdacity()
        with self.assertRaises(NoSuchElementException, msg="test_verifyValidSignUp Failed"):
            time.sleep(3)
            self.screenshot.takeScreenShot(self.screenshotName)
            self.signUpPage.invalidRegistrationMessage()

    def test_verifySignUpWithInvalidEmail(self):
        self.signUpPage.setEmail(self.dic_prop.get("user_email"))
        self.signUpPage.setFirstName(self.dic_prop.get("invalid_first_name"))
        self.signUpPage.setLastName(self.dic_prop.get("invalid_last_name"))
        self.signUpPage.setPassword(self.dic_prop.get("user_password"))
        self.signUpPage.setConfirmPassword(self.dic_prop.get("user_password"))
        self.signUpPage.clickSubmitButton()
        time.sleep(3)
        self.screenshot.takeScreenShot(self.screenshotName)
        self.assertEqual(self.signUpPage.invalidRegistrationMessage(), "This email is already registered",
                         msg="test_verifySignUpWithInvalidEmail Failed")

    def test_verifySignUpWithInvalidPassword(self):
        self.signUpPage.setEmail(self.dic_prop.get("user_email"))
        self.signUpPage.setFirstName(self.dic_prop.get("invalid_first_name"))
        self.signUpPage.setLastName(self.dic_prop.get("invalid_last_name"))
        self.signUpPage.setPassword(self.dic_prop.get("invalid_password"))
        self.signUpPage.setConfirmPassword(self.dic_prop.get("invalid_password"))
        self.signUpPage.clickSubmitButton()
        time.sleep(3)
        self.screenshot.takeScreenShot(self.screenshotName)
        self.assertEqual(self.signUpPage.invalidRegistrationMessage(), "Password is known to be too common.",
                         msg="test_verifySignUpWithInvalidPassword Failed")
