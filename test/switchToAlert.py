import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    link = 'http://suninjuly.github.io/alert_accept.html'
    browser.get(link)

    #нажимаем на кнопку
    button1 = browser.find_element(By.TAG_NAME, 'button')
    button1.click()

    #переключаемся на алерт и подтверждаем его
    alert = browser.switch_to.alert
    alert.accept()

    #вычисляем капчу для роботов
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    sum = calc(x)

    #записываем капчу в инпут
    result = browser.find_element(By.ID, 'answer')
    result.send_keys(sum)

    #нажимаем на кнопку подтверждения
    button2 = browser.find_element(By.CLASS_NAME, 'btn.btn-primary')
    button2.click()

finally:
    time.sleep(10)
    browser.quit()