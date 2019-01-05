
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-extensions")


driver = webdriver.Chrome(options=chrome_options)
#driver = webdriver.Chrome()

driver.set_page_load_timeout(100)

# Implicit Waits
#driver.implicitly_wait(10)


driver.get("https://google.com")


print(driver.title)

driver.find_element_by_name("q").send_keys("Automation step by step")

# Expicit Waits
#wait = WebDriverWait(driver,10)
#element = wait.until(EC.element_to_be_clickable((By.NAME, "btnk")))

driver.find_element_by_xpath("//*[@id='tsf']/div[2]/div/div[3]/center/input[1]").click()

print(driver.title)


print("Test completed")

driver.close()
driver.quit()