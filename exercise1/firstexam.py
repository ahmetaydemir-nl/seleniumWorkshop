import time

from selenium import webdriver


def test_selenium():
    browser = webdriver.Chrome()
    browser.get("http://vinwij.nl/selenium/form.html")
    checkbox = browser.find_element_by_xpath('//input[@id="trek"]')
    checkbox.click()
    time.sleep(3)
    #browser.quit()
