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

@step("I login")
def login_test(step):
    emailInput = world.browser.find_element_by_xpath("//input[@name='email']")
    emailInput.send_keys("rkhan@distribion.com")
    passwordInput = world.browser.find_element_by_xpath("//input[@name='password']")
    passwordInput.send_keys("#Cinco5")
    loginButton = world.browser.find_element_by_xpath("//input[@type='submit']")
    loginButton.click()

@step("I go to mam")
def goto_mam(step):
    actionhover = world.browser.find_element_by_xpath("//li[@class='ui-state-default']")
    hoverMenu = ActionChains(world.browser).move_to_element(actionhover)
    hoverMenu.perform()
    world.browser.find_element_by_xpath("//a[@href='index.php?p=mam3.browse']").click()

@step('I search for template name "(.*)"')
def search_for_keyword(step, keyword):
    searchBarClear = world.browser.find_element_by_xpath(".//*[@id='mam3_keyword_search']")
    searchBarClear.clear()
    searchBar = world.browser.find_element_by_xpath(".//*[@id='mam3_keyword_search']")
    searchBar.send_keys(keyword)

@step("I enter a new email address")
def enter_email(step):
    emailField = world.browser.find_element_by_xpath("//*[@name]='email']")
    emailField.send_keys("newuser" + str(randint(0,999)) + "@mailinator.com")

