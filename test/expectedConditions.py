import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome()

try:
    # Setting url link
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser.get(link)

    # Calculate
    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))

    #  Expecting a price of 100$
    price = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, 'price'), '$100')
    )

    # Find button and click on it
    browser.find_element(By.XPATH, "//button[@id='book']").click()

    # Get text of calculating result
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    sum = calc(x)

    # Finding input and send calc result
    browser.find_element(By.ID, "answer").send_keys(sum)

    # Finding the button and click on it
    browser.find_element(By.XPATH, '//button[@type="submit"]').click()

    # Parsing text from alert
    switchAlert = browser.switch_to.alert
    alertText = switchAlert.text
    print(alertText)

finally:
    time.sleep(5)
    browser.quit()
