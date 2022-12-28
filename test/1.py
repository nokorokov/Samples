import math
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome()
def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

browser.get("http://suninjuly.github.io/explicit_wait2.html")

price = WebDriverWait(browser, 12).until(
    EC.text_to_be_present_in_element((By.ID, 'price'), '$100')
)
print(price)
browser.find_element(By.XPATH, "//button[@id='book']").click()

#находим елемент х и расчитываем его
x_element = browser.find_element(By.ID, "input_value")
x = x_element.text
sum = calc(x)

#находим инпут и записываем в него ответ
input = browser.find_element(By.ID, "answer")
input.send_keys(sum)

#нажимаем на кнопку подтверждения
button2 = browser.find_element(By.XPATH, '//button[@type="submit"]')
button2.click()

#Парсим текст из алерта
switchAlert = browser.switch_to.alert
alertText = switchAlert.text
print(alertText)

time.sleep(5)
