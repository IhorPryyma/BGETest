import unittest

from selenium.common.exceptions import NoSuchWindowException

import util.Logger as cl
import logging

from base.EnvironmentSetup import EnvironmentSetup
from base.PageFactory import PageFactory
from pages.SignUpPage import SignUpPage
from pages.SignInPage import SignInPage


class HomePageTest(EnvironmentSetup):

    log = cl.customLogger(logging.DEBUG)

    def setUp(self):
        super().setUp()
        page_obj = PageFactory()
        self.homePage = page_obj.createPage("home", self.driver, self.dic_prop)

    def test_verifyHomePageTitle(self):
        title = self.homePage.validatHomePageTitle()
        self.assertTrue(title == "Udacity - Free Online Classes & Nanodegrees | Udacity", msg="test_verifyHomePageTitle Failed")

    def test_verifySignInIsDisplayed(self):
        self.assertTrue(self.homePage.getSignIn().is_displayed(), msg="test_verifySignInIsDisplayed Failed")

    def test_verifySignUpIsDisplayed(self):
        self.assertTrue(self.homePage.getSignUp().is_displayed(), msg="test_verifySignUpIsDisplayed Failed")

    def test_verifySignInButton(self):
        login = self.homePage.clickToSignIn()
        self.assertIsInstance(login, SignInPage, msg="test_verifySignInButton Failed")

    def test_verifySignUpButton(self):
        register = self.homePage.clickToSignUp()
        self.assertIsInstance(register, SignUpPage, msg="test_verifySignUpButton Failed")


if __name__ == "__main__":
    unittest.main()
