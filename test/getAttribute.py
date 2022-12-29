from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

browser = webdriver.Chrome()

try:
    # Setting url link
    link = "http://suninjuly.github.io/get_attribute.html"
    browser.get(link)

    # Calculate
    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))

    # Get text of calculating result
    x_element = browser.find_element(By.XPATH, "//img[@id='treasure']")
    box = x_element.get_attribute('valuex')
    sum = calc(box)

    # Finding input and send calc result
    browser.find_element(By.ID, 'answer').send_keys(sum)

    # Finding checkbox and radio after click on them
    browser.find_element(By.ID, "robotsRule").click()
    browser.find_element(By.ID, "robotCheckbox").click()

    # Finding the button and click on it
    browser.find_element(By.CLASS_NAME, "btn.btn-default").click()

finally:
    time.sleep(10)
    browser.quit()