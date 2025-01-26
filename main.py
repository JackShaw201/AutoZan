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
        config.add(comment("https://github.com/JackShaw201/autozan"))

        config.add("qq", "8888888888") # 默认QQ号
        config.add("loginmode", 0)

        with open(CONFIGFILE, "w", encoding="utf-8") as fp:
            dump(config, fp) # 写入配置文件
    else:
        pass

def parse_config(key):
    '''解析配置文件'''
    with open(CONFIGFILE, "r", encoding="utf-8") as fp:
        config = load(fp)
    return config.item(key)

def save_config(qq, loginmode) -> None:
    config = document()

    config.add(comment("autozan config file"))
    config.add(comment("© 2025 by XShaw201"))
    config.add(comment("https://github.com/JackShaw201/autozan"))

    config.add("qq", qq)
    config.add("loginmode", loginmode)

    with open(CONFIGFILE, "w", encoding="utf-8") as fp:
        dump(config, fp) # 之所以将配置文件重新写入一遍，是因为 tomlkit 库似乎没有更新配置参数的方法

if __name__ == "__main__":
    init_config()

    root = maliang.Tk(size=(600, 400), title="QQ空间自动点赞 v0.1", icon="favicon.ico")
    root.center()
    root.resizable(0, 0)

    cv = maliang.Canvas(root, auto_zoom=True, auto_update=True)
    cv.place(width=800, height=600, x=0, y=0)

    # QQ号输入框
    maliang.Text(cv, (10, 30), text="QQ号：", anchor="w")
    input1 = maliang.InputBox(cv, (80, 10), size=(140, 40))
    input1.append(parse_config("qq"))

    # 密码输入框
    maliang.Text(cv, (230, 30), text="密码：", anchor="w")
    input2 = maliang.InputBox(cv, (290, 10), size=(300, 40), show="*")

    # Cookie 输入框
    maliang.Text(cv, (10, 80), text="Cookie：", anchor="w")
    input3 = maliang.InputBox(cv, (90, 60), size=(500, 40))

    # 登录方式选择
    maliang.Text(cv, (10, 315), text="登录方式：", anchor="w")
    sb = maliang.SegmentedButton(cv, (110, 291), text=("快捷登录", "密码登录", "Cookie 登录"), default=parse_config("loginmode"))

    b = maliang.Button(cv, (270, 350), size=(60, 40), text="开始", command=lambda: run(input1.get(), sb.get()))

    root.at_exit(lambda: save_config(input1.get(), sb.get()))
    root.mainloop()