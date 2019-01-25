import unittest

import util.Logger as cl
import logging

from pages.SignUpPage import SignUpPage
from pages.HomePage import HomePage
from pages.SignInPage import SignInPage


class HomePageTest(unittest.TestCase):

    log = cl.customLogger(logging.DEBUG)
    log.debug("---------------------------")
    log.debug("HomePageTestCase is running")
    log.debug("---------------------------")

    def setUp(self):
        self.homePage = HomePage()
        self.driver = self.homePage.driver

    def test_homePageTitleTest(self):
        title = self.homePage.validatHomePageTitle()
        self.assertEqual(title, "Udacity - Free Online Classes & Nanodegrees | Udacit", msg="test_homePageTitleTest Failed")

    def test_validateSignInButton(self):
        login_obj = self.homePage.clickToSignIn()
        self.assertIs(login_obj, SignInPage, msg="test_validateSignInButton Failed")

    def test_validateSignUpButton(self):
        register_obj = self.homePage.clickToSignUp()
        self.assertIs(register_obj, SignUpPage, msg="test_validateSignUpButton Failed")



    def tearDown(self):
        self.driver.quit()
