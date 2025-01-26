from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def run(qq, loginmode):
    driver = webdriver.Chrome()
    driver.get("https://user.qzone.qq.com/" + qq  + "/infocenter")