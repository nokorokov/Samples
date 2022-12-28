from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
browser = webdriver.Chrome()


try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser.get(link)
    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))

    x_element = browser.find_element(By.XPATH, "//img[@id='treasure']")
    box = x_element.get_attribute('valuex')
    sum = calc(box)

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