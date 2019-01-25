import logging
import random

import util.Logger as cl


class UserGenerator:
    log = cl.customLogger(logging.DEBUG)

    def __init__(self):
        self._base = None
        self._email = None
        self._password = None
        self._number = None
        self._name = None

    def generateName(self):
        self._base = "test_user"
        self._number = random.randint(100, 1000)
        self._name = self._base + str(self._number)
        self.log.debug("User is created - " + self._name)
        return self._name

    def generateEmail(self):
        if self._name:
            self.log.debug("New email for user is created - {}@test.com".format(self._name))
            return self._name + "@test.com"
        else:
            return self.generateName() + "@test.com"

    def generatrPassword(self):
        if self._name:
            self._password = self._name + "pass"
            self.log.debug("New password for user is created - {}".format(self._password))
            return self._password
        else:
            return self.generateName()
