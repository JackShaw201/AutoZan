from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from tkinter import messagebox
import maliang

options = webdriver.ChromeOptions()
driver = None

def run(qq: str, loginmode: int | None, b2: maliang.Button):
    if loginmode == 0:
        messagebox.showinfo("提示", "请手动点击头像快捷登录！")
    b2.forget(False)
    driver = webdriver.Chrome(options=options)
    driver.get("https://user.qzone.qq.com/" + qq + "/infocenter")
    # likebtn = driver.find_elements(By.CLASS_NAME, "qz_like_btn_v3")
    # for i in likebtn:
    #     i.click()

def stop(b2: maliang.Button):
    driver.close()
    b2.forget()
