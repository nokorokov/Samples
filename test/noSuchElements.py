from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "http://suninjuly.github.io/registration1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element(By.XPATH, "//input[@placeholder='Input your first name']")
    button.send_keys("example")

    button = browser.find_element(By.XPATH, "//input[@placeholder='Input your last name']")
    button.send_keys("example")

    button = browser.find_element(By.CLASS_NAME, "form-control.third")
    button.send_keys("example@example.com")

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    time.sleep(1)

    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    welcome_text = welcome_text_elt.text

    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    time.sleep(30)
    browser.quit()
