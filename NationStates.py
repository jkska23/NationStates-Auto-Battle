from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

path = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(path)

s = []

try:
    with open("info.txt") as f:
        s = f.read().split("\n") # email, pw, web link
except FileNotFoundError:
    print("File not found")

# opens browser
driver.get(s[2])
time.sleep(3)

# clicks on login element
login = driver.find_element(By.CLASS_NAME, 'icon-login')
login.click()

time.sleep(1)

# username input
email = driver.find_element(By.NAME, 'nation')
email.send_keys(s[0])

# password input
password = driver.find_element(By.NAME, 'password')
password.send_keys(s[1]) 
password.send_keys(Keys.RETURN)

time.sleep(1)

# region
region = driver.find_element(By.CLASS_NAME, 'icon-flag-empty').click()

time.sleep(1)

# target user
target = driver.find_elements(By.CLASS_NAME, 'nlink')
for i in target:
    if (i.text==s[3]):
        i.click()

time.sleep(1)

# clicks on target icon

"""
icons = driver.find_elements(By.XPATH, '//a[@href="https://www.nationstates.net/page=challenge?entity_name=sterza"]')
for i in icons:
    if (i.text=="Challenge"):
        i.click()

driver.find_element(By.CLASS_NAME, 'navbaricon icon-target').click()
uOptions = driver.find_elements(By.TAG_NAME, 'a')

for i in uOptions:
    if (i.text=="/page=challenge?entity_name=sterza"):
        i.click()
"""
time.sleep(3)

driver.quit()

# driver.close() close tab
# driver.quit() quits browser
# driver.back() # back a page
# driver.forward() # forward a page
# element.clear() if it already had keys sent, then will append to it

#password = WebDriverWait(driver, 10).until(
#    EC.presence_of_element_located((By.NAME, 'password'))
#)
