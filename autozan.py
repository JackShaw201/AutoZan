import time
import threading
from tkinter import messagebox

import maliang
from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-automation'])
options.add_argument("--headless")
driver = None

def run(qq: str, interval: int, loginmode: int | None, b2: maliang.Button):
    b2.forget(False)
    try:
        global driver
        driver = webdriver.Chrome(options=options)
        driver.implicitly_wait(10)
        if loginmode == 0:
            driver.get("https://xui.ptlogin2.qq.com/cgi-bin/xlogin?proxy_url=https%3A//qzs.qq.com/qzone/v6/portal/proxy.html&daid=5&&hide_title_bar=1&low_login=0&qlogin_auto_login=1&no_verifyimg=1&link_target=blank&appid=549000912&style=22&target=self&s_url=https%3A%2F%2Fqzs.qzone.qq.com%2Fqzone%2Fv5%2Floginsucc.html%3Fpara%3Dizone%26specifyurl%3Dhttp%253A%252F%252Fuser.qzone.qq.com%252F" + qq + "%252Finfocenter&pt_qr_app=手机QQ空间&pt_qr_link=http%3A//z.qzone.com/download.html&self_regurl=https%3A//qzs.qq.com/qzone/v6/reg/index.html&pt_qr_help_link=http%3A//z.qzone.com/download.html&pt_no_auth=1")
            face = driver.find_element(By.CLASS_NAME, "face")
            face.click()
        while True:
            driver.find_element(By.ID, "tab_menu_friend").click()
            likebtn = driver.find_elements(By.CLASS_NAME, "qz_like_btn_v3")
            for i in likebtn:
                if i.get_attribute("data-islike") == "0":
                    i.click()
                else:
                    continue
            time.sleep(interval * 60)
            driver.refresh()
    finally:
        driver.quit()
        b2.forget()

def start(qq: str, interval: int, loginmode: int | None, b2: maliang.Button):
    threading.Thread(target=run, args=(qq, interval, loginmode, b2)).start()

def stop(b2: maliang.Button):
    driver.quit()
    b2.forget()
