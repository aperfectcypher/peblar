import os
import sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

ip = sys.argv[1]
url = f"http://{ip}/system/3"
password = sys.argv[2]
if len(sys.argv) != 3:
    print("Usage: python peblar_amps.py <ip> <password>")
    sys.exit(1)
    
os.environ['MOZ_HEADLESS'] = '1'
driver = webdriver.Firefox()
driver.get(url)

# Login
wait = WebDriverWait(driver, 10)
element = wait.until(EC.presence_of_element_located((By.ID, 'password')))
pass_field = driver.find_element(By.ID, "password")
pass_field.send_keys(password)

button_xpath = "//button[contains(text(), 'Sign in')]"
button = driver.find_element(By.XPATH, button_xpath)
button.click()

# Wait to find at least on current measurement (ending in ' A')
table_xpath = "//div[contains(text(), ' A')]"
element = wait.until(EC.presence_of_element_located((By.XPATH, table_xpath)))

# get all current measurements
current_measurements = driver.find_elements(By.XPATH, "//div[contains(text(), ' A')]")

# Print the 3 fist current measurements
for i in range(3):
    print(current_measurements[i].text)

driver.close()