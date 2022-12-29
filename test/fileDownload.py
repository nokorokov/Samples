import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()

try:
    # Setting url link
    link = 'http://suninjuly.github.io/file_input.html'
    browser.get(link)

    # Filling in the required fields
    browser.find_element(By.NAME, 'firstname').send_keys('Rudolf')
    browser.find_element(By.NAME, 'lastname').send_keys("Snegov")
    browser.find_element(By.NAME, 'email').send_keys("ex@ex.com")

    # File transfer
    fileButt = browser.find_element(By.NAME, 'file')
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_name = "test.txt"
    file_path = os.path.join(current_dir, file_name)
    fileButt.send_keys(file_path)

    # Finding the button and click on it
    browser.find_element(By.CLASS_NAME, 'btn.btn-primary').click()

finally:
    time.sleep(10)
    browser.quit()