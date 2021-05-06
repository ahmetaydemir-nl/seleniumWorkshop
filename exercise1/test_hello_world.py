from selenium import webdriver


def test_hello_world():
    browser = webdriver.Chrome()
    browser.get("https://amazon.com")
    browser.quit()

