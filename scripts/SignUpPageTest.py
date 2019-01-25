import unittest

from pages.HomePage import HomePage
from pages.SignInPage import SignInPage
from pages.ProfilePage import ProfilePage
from pages.SignUpPage import SignUpPage


class SignUpPageTest(unittest.TestCase):


    def setUp(self):
        self.homePage = HomePage()
        self.driver = self.homePage.driver
        prop = self.homePage.dic_prop
        self.homePage.clickToSignUp()
        self.signUpPage = SignUpPage(self.driver, prop)

    def test_signUpPageTitleTest(self):
        title = self.signUpPage.validateSignUpPageTitle()
        self.assertEqual(title, "Sign Up - Udacity")

    def test_validateSignUpToUdacity(self):
        profile_obj = self.signUpPage.signUpToUdacity()
        self.assertIs(profile_obj, ProfilePage)

    def tearDown(self):
        self.driver.quit()
