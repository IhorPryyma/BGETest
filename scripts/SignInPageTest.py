import unittest

from pages.HomePage import HomePage
from pages.SignInPage import SignInPage
from pages.ProfilePage import ProfilePage


class SignInPageTest(unittest.TestCase):


    def setUp(self):
        self.homePage = HomePage()
        self.driver = self.homePage.driver
        prop = self.homePage.dic_prop
        self.homePage.clickToSignIn()
        self.signInPage = SignInPage(self.driver, prop)

    def test_signInPageTitleTest(self):
        title = self.signInPage.validateSignInPageTitle()
        self.assertEqual(title, "Sign In - Udacity")

    def test_validateSignInToUdacity(self):
        profile_obj = self.signInPage.signInToUdacity()
        self.assertIs(profile_obj, ProfilePage)

    def tearDown(self):
        self.driver.quit()
