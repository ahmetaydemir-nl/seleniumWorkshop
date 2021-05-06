import time

from selenium import webdriver

def test_selenium():
    browser = webdriver.Chrome()
    browser.get("http://vinwij.nl/selenium/factuur.html")
    element_amount = browser.find_element_by_css_selector('#tot_amount')
    assert element_amount.text =='Totaal: € 392,30', 'lsjdflsjdflksd'
    time.sleep(3)
    #browser.quit()


