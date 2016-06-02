from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains


driver = webdriver.Firefox()
driver.get('https://www.dartlang.org/samples/dnd/')

draggable = driver.find_element_by_xpath(".//*[@id='columns']/div[1]")
droppable = driver.find_element_by_xpath(".//*[@id='columns']/div[2]")

action_chains = ActionChains(driver)
action_chains.drag_and_drop(draggable, droppable).perform()

driver.quit()
