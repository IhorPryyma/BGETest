import sys
import unittest

from scripts.HomePageTest import HomePageTest
from scripts.SignInPageTest import SignInPageTest


def suite():
    suite = unittest.TestSuite()
    suite.addTest(HomePageTest("test_homePageTitleTest"))
    suite.addTest(HomePageTest("test_validateSignInButton"))
    suite.addTest(HomePageTest("test_validateSignUpButton"))
    suite.addTest(SignInPageTest("test_signInPageTitleTest"))

    return suite


if __name__ == "__main__":
    runner = unittest.TextTestRunner()

    runner.run(suite())
    result = unittest.TextTestResult(stream=sys.stdout, descriptions=True, verbosity=1)

    print(result)
