import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()

try:
    # Setting url link
    link = 'http://suninjuly.github.io/alert_accept.html'
    browser.get(link)

    # Calculate
    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))


    # Finding the button and click on it
    browser.find_element(By.TAG_NAME, 'button').click()

    # Switch to alert and accept it
    alert = browser.switch_to.alert
    alert.accept()

    # Get text of calculating result
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    sum = calc(x)

    # Finding input and send calc result
    browser.find_element(By.ID, 'answer').send_keys(sum)

    # Finding the button and click on it
    browser.find_element(By.CLASS_NAME, 'btn.btn-primary').click()

finally:
    time.sleep(10)
    browser.quit()