import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()

try:
    # Setting url link
    link='http://suninjuly.github.io/redirect_accept.html'
    browser.get(link)

    # Calculate
    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))

    # Find the element and click
    browser.find_element(By.CLASS_NAME, 'trollface.btn.btn-primary').click()

    # Setting name the window and going to second
    first_window = browser.window_handles[0]
    second_window = browser.window_handles[1]
    switching = browser.switch_to.window(second_window)

    # Get text of calculating result
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    sum = calc(x)

    # Writting captcha in input
    browser.find_element(By.ID, 'answer').send_keys(sum)

    # Finding the button and click on it
    button2 = browser.find_element(By.CLASS_NAME, 'btn.btn-primary')
    button2.click()

    # Parsing text from alert
    switchAlert = browser.switch_to.alert
    alertText = switchAlert.text

finally:
    time.sleep(2)
    browser.quit()
