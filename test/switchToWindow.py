import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    link='http://suninjuly.github.io/redirect_accept.html'
    browser = webdriver.Chrome()
    browser.get(link)

    #переходим на страницу и нажимаем кнопку далее
    button1 = browser.find_element(By.CLASS_NAME, 'trollface.btn.btn-primary')
    button1.click()

    #Задаем окнам значения 0 и 1, и переключаемся на второе окно
    first_window = browser.window_handles[0]
    second_window = browser.window_handles[1]
    switching = browser.switch_to.window(second_window)

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

    #Парсим текст из алерта
    switchAlert = browser.switch_to.alert
    alertText = switchAlert.text
    print(alertText)

finally:
    time.sleep(2)
    browser.quit()
