from lettuce import *
from lettuce_webdriver.util import assert_false
from lettuce_webdriver.util import AssertContextManager
from selenium.webdriver import ActionChains
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from random import randint
from nose.tools import assert_equals

@step('When I enter a website "(.*)"')
def enterSite(step, keyword):
    site = world.browser.find_element_by_xpath("//input[@name='url']")
    site.send_keys(keyword)

@step("I start my test")
def enderTest(step):
    enterButton = world.browser.find_element_by_xpath("//input[@type='submit']")
    enterButton.click()

@step('I enter "(.*)" as Test Name')
def testName(step, keyword):
    enterTestName = world.browser.find_element_by_id("edit-test-name")
    enterTestName.send_keys("Google Test")
   

@step('I search for "(.*)" in the dropdown')
def dropdown(step, keyword):
    select = world.browser.find_element_by_id("edit-tests-type-2")
    for option in select.find_element_by_tag_name(option):
        if option.text == (keyword):
            option.click()
            break
        

     
