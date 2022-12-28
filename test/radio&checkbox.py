from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))
try:
    link = "https://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    sum = calc(x)

    y = browser.find_element(By.ID, 'answer')
    y.send_keys(sum)

    checkbox = browser.find_element(By.ID, "robotsRule")
    checkbox.click()

    radio = browser.find_element(By.ID, "robotCheckbox")
    radio.click()

    button = browser.find_element(By.CLASS_NAME, "btn.btn-default")
    button.click()

finally:
    time.sleep(10)
    browser.quit()





