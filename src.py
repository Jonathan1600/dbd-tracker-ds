import os
from selenium import webdriver

PATH = "C:\Program Files (x86)\chromedriver.exe"

driver = webdriver.Chrome(PATH)

driver.get("https://dbd-stats.net/profile/76561199071307129")
