
from selenium import webdriver
browser = webdriver.Firefox()
browser.get('https://google.com')

print(browser.title)
inputElement = browser.find_element_by_name("q")

inputElement.send_keys("Avengers")
inputElement.submit()
print(browser.title)
