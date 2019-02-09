import logging
import sys
import unittest
import util.Logger as cl

from scripts.ProfilePageTest import ProfilePageTest
from scripts.HomePageTest import HomePageTest
from scripts.SignInPageTest import SignInPageTest
from scripts.SignUpPageTest import SignUpPageTest

log = cl.customLogger(logging.DEBUG)


def suite():
    suite = unittest.TestSuite()
    suite.addTest(HomePageTest("test_verifyHomePageTitle"))
    suite.addTest(HomePageTest("test_verifySignInIsDisplayed"))
    suite.addTest(HomePageTest("test_verifySignUpIsDisplayed"))
    suite.addTest(HomePageTest("test_verifySignInButton"))
    suite.addTest(HomePageTest("test_verifySignUpButton"))
    suite.addTest(SignInPageTest("test_verifySignInPageTitle"))
    suite.addTest(SignInPageTest("test_verifyValidSignIn"))
    suite.addTest(SignInPageTest("test_verifyInvalidSignIn"))
    suite.addTest(SignUpPageTest("test_verifySignUpPageTitle"))
    suite.addTest(SignUpPageTest("test_verifyValidSignUp"))
    suite.addTest(SignUpPageTest("test_verifySignUpWithInvalidEmail"))
    suite.addTest(SignUpPageTest("test_verifySignUpWithInvalidPassword"))
    suite.addTest(ProfilePageTest("test_verifyProfilePageTitle"))
    suite.addTest(ProfilePageTest("test_verifyElementsOfProfilePage"))
    suite.addTest(ProfilePageTest("test_verifyLogout"))

    return suite


if __name__ == "__main__":

    runner = unittest.TextTestRunner(verbosity=2, descriptions=True, stream=sys.stdout)
    result = runner.run(suite())
    for line in result.failures:
        for info in line:
            log.error(str(info))
