import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

try:
    link = 'https://suninjuly.github.io/selects2.html'
    browser = webdriver.Chrome()
    browser.get(link)

    num1 = browser.find_element(By.XPATH, '//span[@id="num1"]')
    num1Text = num1.text
    num2 = browser.find_element(By.XPATH, '//span[@id="num2"]')
    num2Text = num2.text


    answer = str(int(num1Text)+int(num2Text))
    print(answer)


    select = Select(browser.find_element(By.XPATH, "//select[@id='dropdown']"))
    select.select_by_value(answer)

    button = browser.find_element(By.CLASS_NAME, 'btn.btn-default')
    button.click()


finally:
    time.sleep(10)
    browser.quit()
