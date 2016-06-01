from selenium import webdriver
from seleniu,.webdriver.common.action_chains import ActionChains



driver = webdriver.Firefox()
driver.get('http://www.seleniumframework.com/Practiceform/')

alertBox = driver.find_element_by_xpath("//button[@id='alert']").click()

alert = driver.switch_to_alert()
