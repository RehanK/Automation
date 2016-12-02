from lettuce import *
import sys, unittest
from lettuce import before, world
from selenium import webdriver
import lettuce_webdriver.webdriver



#@before.all  #This hook is ran before lettuce look for and load feature files
# def say_hello():
#     print "Hello there!"
#     print "Lettuce will start to run tests right now..."

@before.each_feature
def setup_browser(step):
     world.browser = webdriver.Firefox()
     world.browser.implicitly_wait(5)

# @before.each_scenario
# def setup_some_scenario(scenario):
# #     world.browser = webdriver.Firefox()
# #     world.browser.implicitly_wait(5)

#@before.each_step
#@after.each_step

#@after.each_scenario

@after.each_feature
def teardown_some_feature(feature):
    if sys.exc_info()[0]:  # Returns the info of exception being handled
            fail_url = world.browser.current_url
            print fail_url
            now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S-%f')
            world.browser.get_screenshot_as_file('/path/to/file/%s.png' % now)
            fail_screenshot_url = 'http://debugtool/screenshots/%s.png' % now
            print fail_screenshot_url
    world.browser.quit()
    print "Completed & exited browser"
    
#@after.all #This hook is ran after lettuce run all features, scenarios and steps
# def say_goodbye(total):
#     print "Congratulations, %d of %d scenarios passed!" % (
#         total.scenarios_ran,
#         total.scenarios_passed
#     )
#     print "Goodbye!"
