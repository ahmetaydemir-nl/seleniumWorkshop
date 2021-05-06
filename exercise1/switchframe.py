import time
from lib2to3.pgen2 import driver

from selenium import webdriver


def test_selenium():
    browser = webdriver.Chrome()
    browser.get("http://vinwij.nl/selenium/frame.html")
    #checkbox = browser.find_elements_by_css_selector('#trek')
    driver.switch_to_frame("#trek")
    #checkbox.click()

    #assert element_trekhaak.text =='Totaal: € 392,30', 'lsjdflsjdflksd'
    time.sleep(3)
    #browser.quit()
