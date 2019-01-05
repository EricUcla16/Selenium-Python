import time
from selenium import webdriver

#if your path variable is not set, use this code below to instatiate a new webdriver

driver = webdriver.Chrome()
driver.set_page_load_timeout(100)
driver.get("https://google.com")
driver.find_element_by_name("q").send_keys("Automation step by step")
driver.find_element_by_xpath("//*[@id='tsf']/div[2]/div/div[3]/center/input[1]").click()


driver2 = webdriver.Firefox()
driver2.set_page_load_timeout(100)
driver2.get("http://yahoo.com")
driver2.find_element_by_xpath("//*[@id='uh-search-box']").send_keys("fart proudly by Ben Franklin")
driver2.find_element_by_xpath("//*[@id='uh-search-button']").click()


time.sleep(3)


driver.close()
driver.quit()

driver2.close()
driver2.quit()

print("Test completed")