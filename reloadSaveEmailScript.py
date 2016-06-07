from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support.ui import Select
import time
from random import randint

driver = webdriver.Firefox()
driver.get("http://swinglecollins.dmplocal.com/main/index.php?p=mainmenu.items.browse")



#login to dmp
emailInput = driver.find_element_by_xpath("//input[@name='email']")
emailInput.send_keys("training@distribion.com")
passwordInput = driver.find_element_by_xpath("//input[@name='password']")
passwordInput.send_keys("*")
loginButton = driver.find_element_by_xpath("//a[@id='login-btn']")
loginButton.click()

menuItemName = driver.find_element_tag_name("Reload a Saved E-mail")
edit = menuItemName.find_element_by_xpath("//a[@title='Edit Item']")
edit.click()

#login
#go to navigation menu items
#edit Reload save email menu item
#change to:
#save
#go to reload saved email
#verify url is updated
