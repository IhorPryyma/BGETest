

class ScreenShot:

    def __init__(self, driver):
        self.driver = driver

    def takeScreenShot(self, ss_name):

        self.driver.save_screenshot(ss_name)
