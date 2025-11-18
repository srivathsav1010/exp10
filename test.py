from selenium import webdriver 
from selenium.webdriver.chrome.service import Service 
from selenium.webdriver.common.by import By 
from selenium.webdriver.common.keys import Keys 
import time
 
chrome_service = Service(r"C:\Program Files\chromedriver-win64\chromedriver.exe") 
driver = webdriver.Chrome(service=chrome_service) 
 
try: 
    # Step 1: Open Google in the browser 
    driver.get("https://www.google.com") 
    # Step 2: Locate the search box using the name attribute 
    search_box = driver.find_element(By.NAME, "q") 
 
    # Step 3: Enter the search term and press Enter 
    search_box.send_keys("https://cmrcet.ac.in/") 
    search_box.send_keys(Keys.RETURN) 
 
    time.sleep(5000) 
 
finally: 
    driver.quit() 