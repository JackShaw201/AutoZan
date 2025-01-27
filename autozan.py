import time
from tkinter import messagebox

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchWindowException, NoSuchElementException, WebDriverException
import maliang

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-automation'])
# options.add_argument("--headless")
driver = None

def run(qq: str, loginmode: int | None, b2: maliang.Button):
    b2.forget(False)
    try:
        global driver
        driver = webdriver.Chrome(options=options)
        if loginmode == 0:
            driver.get("https://xui.ptlogin2.qq.com/cgi-bin/xlogin?proxy_url=https%3A//qzs.qq.com/qzone/v6/portal/proxy.html&daid=5&&hide_title_bar=1&low_login=0&qlogin_auto_login=1&no_verifyimg=1&link_target=blank&appid=549000912&style=22&target=self&s_url=https%3A%2F%2Fqzs.qzone.qq.com%2Fqzone%2Fv5%2Floginsucc.html%3Fpara%3Dizone%26specifyurl%3Dhttp%253A%252F%252Fuser.qzone.qq.com%252F" + qq + "%252Finfocenter&pt_qr_app=手机QQ空间&pt_qr_link=http%3A//z.qzone.com/download.html&self_regurl=https%3A//qzs.qq.com/qzone/v6/reg/index.html&pt_qr_help_link=http%3A//z.qzone.com/download.html&pt_no_auth=1")
            face = driver.find_element(By.CLASS_NAME, "face")
            face.click()
        while True:
            time.sleep(1)
            likebtn = driver.find_elements(By.CLASS_NAME, "qz_like_btn_v3")
            print(likebtn.__len__())
    except NoSuchWindowException as e:
        messagebox.showerror("错误", str(e))
    except NoSuchElementException as e:
        messagebox.showerror("错误", str(e))
    except WebDriverException as e:
        messagebox.showerror("错误", str(e))
    finally:
        driver.quit()
        b2.forget()

    # likebtn = driver.find_elements(By.CLASS_NAME, "qz_like_btn_v3")
    # for i in likebtn:
    #     i.click()

def stop(b2: maliang.Button):
    driver.quit()
    b2.forget()
