import math
from selenium import webdriver
import time
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    #переходим на нужную нам страницу
    link = "http://SunInJuly.github.io/execute_script.html"
    browser.get(link)

    #находим елемент х и расчитываем его
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    sum = calc(x)

    #находим инпут и записываем в него ответ
    input = browser.find_element(By.ID, "answer")
    input.send_keys(sum)

    #находим нужный чекбокс и отмечаем его
    checkbox = browser.find_element(By.ID, 'robotCheckbox')
    checkbox.click()

    #находим нужный радиобатон и переключаем его
    radiobatton = browser.find_element(By.ID, "robotsRule")
    browser.execute_script('return arguments[0].scrollIntoView(true);', radiobatton)
    radiobatton.click()

    #скролим страницу вниз
    button = browser.find_element(By.TAG_NAME, "button")
    browser.execute_script('return arguments[0].scrollIntoView(true);', button)
    button.click()



finally:
    time.sleep(10)
    browser.quit()