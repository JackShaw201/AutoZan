from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

def run(qq, loginmode):
    driver = webdriver.Chrome()
    driver.get("https://user.qzone.qq.com/" + qq  + "/infocenter")
    time.sleep(10)
    likebtn = driver.find_elements(By.CLASS_NAME, "qz_like_btn_v3")
    for i in likebtn:
        i.click()