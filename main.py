import maliang
import os
from tomlkit import document
from tomlkit import comment
from tomlkit import dump
from tomlkit import load
from autozan import run

CONFIGFILE = "config.toml" # 定义配置文件名

def init_config():
    '''初始化配置文件'''
    if not os.path.exists(CONFIGFILE): # 如果配置文件不存在则创建一个默认的配置文件
        config = document()

        config.add(comment("autozan config file"))
        config.add(comment("© 2025 by XShaw201"))
        config.add("qq", "8888888888") # 默认QQ号
        with open(CONFIGFILE, "w", encoding="utf-8") as fp:
            dump(config, fp) # 写入配置文件
    else:
        pass
    with open(CONFIGFILE, "r") as fp:
        config = load(fp) # 读取配置文件
    return config

def read_config(config):
    '''读取配置文件'''
    return config.value

if __name__ == "__main__":
    config = init_config()

    root = maliang.Tk(size=(600, 400), title="QQ空间自动点赞", icon="favicon.ico")
    root.center()
    root.resizable(0, 0)

    cv = maliang.Canvas(root, auto_zoom=True, auto_update=True)
    cv.place(width=800, height=600, x=0, y=0)

    b = maliang.Button(cv, (270, 350), size=(60, 40), text="开始", command=lambda: run())

    root.mainloop()