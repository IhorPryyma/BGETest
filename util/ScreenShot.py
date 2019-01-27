

class ScreenShot:

    def __init__(self, driver):
        self.driver = driver

    def takeScreenShot(self, ss_name):
        # result_dir = "~/user/PycharmProjects/BGEWebAutomation/TestSuits/Results/"
        self.driver.save_screenshot(ss_name)
        # self.driver.save_screenshot(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'Results', ss_name))




