
from pages.HomePage import HomePage
from pages.ProfilePage import ProfilePage
from pages.SignInPage import SignInPage
from pages.SignUpPage import SignUpPage


class PageFactory:

    def createPage(self, pageName, driver, dic_prop):
        if pageName == "home":
            return HomePage(driver, dic_prop)
        elif pageName == "signin":
            HomePage(driver, dic_prop).clickToSignIn()
            return SignInPage(driver, dic_prop)
        elif pageName == "signup":
            HomePage(driver, dic_prop).clickToSignUp()
            return SignUpPage(driver, dic_prop)
        elif pageName == "profile":
            HomePage(driver, dic_prop).clickToSignIn().signInToUdacity()
            return ProfilePage(driver, dic_prop)
        else:
            raise ValueError("Unknown page")
