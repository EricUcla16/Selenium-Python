import time
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

firefox_options = Options()
firefox_options.add_argument("--headless")

driver2 = webdriver.Firefox(options=firefox_options)
driver2.set_page_load_timeout(100)
driver2.get("http://yahoo.com")

print(driver2.title)

driver2.find_element_by_xpath("//*[@id='uh-search-box']").send_keys("fart proudly by Ben Franklin")
driver2.find_element_by_xpath("//*[@id='uh-search-button']").click()


print(driver2.title)


time.sleep(3)


driver2.close()
driver2.quit()

print("Test completed")