import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

try:
    link = 'http://suninjuly.github.io/file_input.html'
    browser = webdriver.Chrome()
    browser.get(link)

    namefield = browser.find_element(By.NAME, 'firstname')
    namefield.send_keys('Rudolf')
    lNamefield = browser.find_element(By.NAME, 'lastname')
    lNamefield.send_keys("Snegov")
    emailField = browser.find_element(By.NAME, 'email')
    emailField.send_keys("ex@ex.com")

    fileButt = browser.find_element(By.NAME, 'file')
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_name = "test.txt"
    file_path = os.path.join(current_dir, file_name)
    fileButt.send_keys(file_path)

    button = browser.find_element(By.CLASS_NAME, 'btn.btn-primary')
    button.click()
finally:
    time.sleep(10)
    browser.quit()