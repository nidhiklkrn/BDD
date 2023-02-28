from behave import *
from selenium import webdriver


@given('Launch chrome browser')
def launchBrowser(context):
    context.driver = webdriver.Chrome(executable_path="Desktop\chromedriver_win32.exe")


@when('open hrm home page')
def openHomePage(context):
    context.driver.get("https://opensource-demo.orangehrmlive.com")

@then('verify that the logo present on page')
def verifylogo(context):
    status = not context.driver.fine_element_by_xpath("//div[@id='divlogo]//img").is_displayed()
    assert status is True

@then('close browser')
def closebrowser(context):
    context.driver.close()

@then('verify that the logo present on page')
def verifyLogo(context):
    status = context.driver.find_element_by_xpath("//div[@id='divLogo']//img").is_displayed()
    assert status is True


@then('close browser')
def closeBrowser(context):
    context.driver.close()