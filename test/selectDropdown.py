import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

browser = webdriver.Chrome()

try:
    # Setting url link
    link = 'https://suninjuly.github.io/selects2.html'
    browser.get(link)

    # Finding int in the page and set them text
    num1 = browser.find_element(By.XPATH, '//span[@id="num1"]')
    num1Text = num1.text
    num2 = browser.find_element(By.XPATH, '//span[@id="num2"]')
    num2Text = num2.text

    # Calculating
    answer = str(int(num1Text)+int(num2Text))
    print(answer)

    # Finding dropdown and select value
    select = Select(browser.find_element(By.XPATH, "//select[@id='dropdown']"))
    select.select_by_value(answer)

    # Finding submit button and click on it
    browser.find_element(By.CLASS_NAME, 'btn.btn-default').click()

finally:
    time.sleep(10)
    browser.quit()
