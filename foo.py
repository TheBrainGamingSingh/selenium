
from selenium import webdriver
browser = webdriver.Firefox()
browser.get('http://127.0.0.1:8000/BVP_PD_2019/admin/import/simple/')



print(browser.title)
