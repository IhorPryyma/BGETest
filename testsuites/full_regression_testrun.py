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
    suite.addTest(HomePageTest("test_homePageTitleTest"))
    suite.addTest(HomePageTest("test_verifySignInButton"))
    suite.addTest(HomePageTest("test_verifySignUpButton"))
    suite.addTest(SignInPageTest("test_signInPageTitleTest"))
    suite.addTest(SignInPageTest("test_verifySignInToUdacity"))
    suite.addTest(SignUpPageTest("test_signUpPageTitleTest"))
    suite.addTest(SignUpPageTest("test_verifySignUpToUdacity"))
    suite.addTest(ProfilePageTest("test_profilePageTitleTest"))
    suite.addTest(ProfilePageTest("test_verifyElementsOfProfilePage"))
    suite.addTest(ProfilePageTest("test_verifyLogout"))

    return suite


if __name__ == "__main__":

    runner = unittest.TextTestRunner(verbosity=2, descriptions=True, stream=sys.stdout)
    result = runner.run(suite())
    for line in result.failures:
        for info in line:
            log.error(str(info))

