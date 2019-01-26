from base.TestBase import TestBase


class ProfilePage(TestBase):

    def __init__(self, driver, prop):
        # super(SignInPage, self).__init__()
        self.driver = driver
        self.dic_prop = prop
