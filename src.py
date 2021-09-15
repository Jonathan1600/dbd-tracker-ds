import os
from selenium import webdriver

PATH = "C:\Program Files (x86)\chromedriver.exe"

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(PATH, options=options)


driver.get("https://dbd-stats.net/profile/76561199071307129")

print(driver.title)

driver.quit()
