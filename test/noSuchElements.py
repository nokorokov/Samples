from selenium import webdriver
from selenium.webdriver.common.by import By
import time

browser = webdriver.Chrome()

try:
    # Setting url link
    link = "http://suninjuly.github.io/registration1.html"
    browser.get(link)

    # Setting required fields and continue
    browser.find_element(By.XPATH, "//input[@placeholder='Input your first name']").send_keys("example")
    browser.find_element(By.XPATH, "//input[@placeholder='Input your last name']").send_keys("example")
    browser.find_element(By.CLASS_NAME, "form-control.third").send_keys("example@example.com")
    browser.find_element(By.CSS_SELECTOR, "button.btn").click()

    time.sleep(1)

    # Finding welcome-text, parsing text and checking itgit
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    welcome_text = welcome_text_elt.text
    print(welcome_text)
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    time.sleep(30)
    browser.quit()
