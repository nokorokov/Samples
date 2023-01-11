import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/"


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()


class TestMainPage1():

    # маркируем тест для смоука, запуск = 'pytest -s -v -m smoke markingPyTest.py'
    @pytest.mark.smoke
    def test_guest_should_see_login_link(self, browser):
        print("start test1")
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, "#login_link")
        print("finish test1")

    # маркируем тест для регрессии, запуск = 'pytest -s -v -m regression markingPyTest.py'
    @pytest.mark.regression
    @pytest.mark.win10 #'pytest -s -v -m "smoke and win10" markingPyTest.py'
    def test_guest_should_see_basket_link_on_the_main_page(self, browser):
        print("start test2")
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, ".basket-mini .btn-group > a")
        print("finish test2")


# Варианты запуска
# pytest -s -v -m regression markingPyTest.py - запуститься регрессионный тест
# pytest -s -v -m "regression and win10" markingPyTest.py запуститься регрессионный тест для Win10
# pytest -s -v -m smoke markingPyTest.py - только смоук