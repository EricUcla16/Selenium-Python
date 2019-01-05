from selenium import webdriver

driver = webdriver.Chrome()
driver.set_page_load_timeout(100)
driver.get("https://google.com")


print(driver.title)


driver.find_element_by_name("q").send_keys("Automation step by step")
driver.find_element_by_xpath("//*[@id='tsf']/div[2]/div/div[3]/center/input[1]").click()


print(driver.title)


print("Test completed")

driver.close()
driver.quit()