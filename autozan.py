from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def run():
    driver = webdriver.Chrome()
    driver.get("https://www.autozan.com/")