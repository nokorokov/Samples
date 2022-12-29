from selenium import webdriver
import unittest
from selenium.webdriver.common.by import By

class OneTest(unittest.TestCase):
    def test_reg1(self):
        browser = webdriver.Chrome()
        link = "http://suninjuly.github.io/registration1.html"
        browser.get(link)

        browser.find_element(By.XPATH, "//input[@placeholder='Input your first name']").send_keys("example")
        browser.find_element(By.XPATH, "//input[@placeholder='Input your last name']").send_keys("example")
        browser.find_element(By.CLASS_NAME, "form-control.third").send_keys("example@example.com")
        browser.find_element(By.CSS_SELECTOR, "button.btn").click()
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text

        self.assertEqual('Congratulations! You have successfully registered!', welcome_text, "No, it`s wrong")


    def test_reg2(self):
        browser = webdriver.Chrome()
        link = "http://suninjuly.github.io/registration2.html"
        browser.get(link)

        browser.find_element(By.XPATH, "//input[@placeholder='Input your first name']").send_keys("example")
        browser.find_element(By.XPATH, "//input[@placeholder='Input your last name']").send_keys("example")
        browser.find_element(By.CLASS_NAME, "form-control.third").send_keys("example@example.com")
        browser.find_element(By.CSS_SELECTOR, "button.btn").click()
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text

        self.assertEqual('Congratulations! You have successfully registered!', welcome_text, "No, it`s wrong")


if __name__ == "__main__":
    unittest.main()