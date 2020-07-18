import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys

options = Options()
options.add_argument("user-data-dir=C:\\Users\\Boxca\\AppData\\Local\\Google\\Chrome\\profiletwo")
driver = webdriver.Chrome(r"C:\Users\Boxca\Downloads\Drivers\chromedriver_win32 (1)\chromedriver.exe", options=options)

# Navigate to search url + search string
search_query = input('what are we watching?')
driver.get("https://www.youtube.com/results?search_query=" + search_query)

# Enumerate through results
for num, element in enumerate(driver.find_elements_by_id("video-title"), start=1):
    print(f"Enter {num} for {element.text}")
    if num == 3:
        break

# Take user input and start video + return url
choice = int(input("Please enter choice from 1 to 3"))
if choice <= 3:
    play = driver.find_elements_by_id('video-title')[choice - 1].click()
    url = driver.find_elements_by_id('video-title')[choice - 1]
    print(url.get_attribute('href'))

else:
    print(f"Please only enter numbers from 1 to 3")


