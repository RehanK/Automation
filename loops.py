
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support.ui import Select
import time
from random import randint

driver = webdriver.Firefox()
driver.get("http://stagingqa.dmplocal.com/main/index.php?p=admin.users.manage")

#login to dmp
emailInput = driver.find_element_by_xpath("//input[@name='email']")
emailInput.send_keys("rkhan@distribion.com")
passwordInput = driver.find_element_by_xpath("//input[@name='password']")
passwordInput.send_keys("")
loginButton = driver.find_element_by_xpath("//input[@type='submit']")
loginButton.click()

#DROP DOWN OPTIONS
#1
#Find the element
#Iterate to get all the options from the dropdown
#Iterate through the list
#For each item in the list, select the current option
#It's necessary to re-select the dropdown on each pass, as the web page has changed

"""select = driver.find_element_by_xpath("//select[@id='comparison']")            
options = select.find_elements_by_tag_name("option")

optionsList = []

for option in options: 
    optionsList.append(option.get_attribute("value"))

for optionValue in optionsList:
    print "starting loop on option: %s" % optionValue

    select = Select(driver.find_element_by_xpath("//select[@id='comparison']"))
    select.select_by_value('start')
"""

#2
#This works!!!, this will select the dropdown option "Begins with" 
select = driver.find_element_by_xpath("//select[@id='comparison']")

for option in select.find_elements_by_tag_name("option"):
    if option.text == "Begins with":
        option.click()
	break


driver.close()
