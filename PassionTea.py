from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support.ui import Select
import time
from random import randint


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

email = driver.find_element_by_xpath("//input[@id='email']")
email.click()
email.send_keys("testemail@mailinator.com")

name = driver.find_element_by_xpath("//input[@id='name']")
name.click()
name.send_keys("Tom")

address = driver.find_element_by_xpath("//textarea[@id='address']")
address.click()
address.send_keys("123 Hallow Dr")
address.send_keys(Keys.RETURN)
address.send_keys("98765, Dallas TX")

select = Select(driver.find_element_by_id('card_type'))
select.select_by_visible_text('American Express')

cardNumber = driver.find_element_by_xpath("//input[@id='card_number']")
cardNumber.click()
cardNumber.send_keys("55555555555")

cardHolderName = driver.find_element_by_xpath("//input[@id='cardholder_name']")
cardHolderName.click()
cardHolderName.send_keys("Tom Bob")

verifiCode = driver.find_element_by_xpath("//input[@id='verification_code']")
verifiCode.click()
verifiCode.send_keys("54321")

placeOrder = driver.find_element_by_xpath("//button[@class='btn btn-primary']")
placeOrder.click()

letsTalk = driver.find_element_by_xpath("//a[@data-url='let-s-talk-tea.html']")
letsTalk.click()
assert "Let's Talk Tea" in driver.title
print "%s" % driver.title


drive.close()
