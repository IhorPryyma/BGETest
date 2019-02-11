import logging
import unittest

import sys,os
sys.path.append(os.path.realpath('..'))

import util.Logger as cl

from scripts.ProfilePageTest import ProfilePageTest
from scripts.HomePageTest import HomePageTest
from scripts.SignInPageTest import SignInPageTest
from scripts.SignUpPageTest import SignUpPageTest

log = cl.customLogger(logging.DEBUG)

def suite():
    suite = unittest.TestSuite()
    suite.addTest(SignInPageTest("test_verifyValidSignIn"))
    suite.addTest(ProfilePageTest("test_verifyLogout"))
    suite.addTest(SignUpPageTest("test_verifyValidSignUp"))

    return suite


if __name__ == "__main__":

    runner = unittest.TextTestRunner(verbosity=2, descriptions=True, stream=sys.stdout)
    result = runner.run(suite())
    for line in result.failures:
        for info in line:
            log.error(str(info))

