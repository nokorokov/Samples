import math
from selenium import webdriver
import time
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()


try:
    # Setting url link
    link = "http://SunInJuly.github.io/execute_script.html"
    browser.get(link)

    # Calculate
    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))

    # Get text of calculating result
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    sum = calc(x)

    # Finding input and send calc result
    browser.find_element(By.ID, "answer").send_keys(sum)

    # Finding checkbox and click on it
    browser.find_element(By.ID, 'robotCheckbox').click()

    # Scroll the page until find the radio button and click on it
    radiobatton = browser.find_element(By.ID, "robotsRule")
    browser.execute_script('return arguments[0].scrollIntoView(true);', radiobatton)
    radiobatton.click()

    # Scroll the page until find the button and click on it
    button = browser.find_element(By.TAG_NAME, "button")
    browser.execute_script('return arguments[0].scrollIntoView(true);', button)
    button.click()


finally:
    time.sleep(10)
    browser.quit()