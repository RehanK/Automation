from selenium import webdriver
from selenium.webdriver.common.keys import Keys



driver = webdriver.Firefox()
driver.get("http://www.practiceselenium.com/")
assert "Welcome" in driver.title
print "%s" % driver.title

ourPassion = driver.find_element_by_xpath("//a[@data-url='our-passion.html']")
ourPassion.click()
assert "Our Passion" in driver.title
print "%s" % driver.title

menu = driver.find_element_by_xpath("//a[@data-url='menu.html']")
menu.click()
assert "Menu" in driver.title
print "%s" % driver.title

greenTea = driver.find_element_by_xpath("//a[@id='wsb-button-00000000-0000-0000-0000-000451955160']")
greenTea.click()
assert "Check Out" in driver.title
print "%s" % driver.title


