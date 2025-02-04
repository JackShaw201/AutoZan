import os

import maliang
from maliang import animation
from tomlkit import document, comment, dump, load

from autozan import start, stop

class Config:
    '''配置文件类'''
    CONFIGFILE = "config.toml" # 定义配置文件名
    def __init__(self):
        '''初始化配置文件'''
        if not os.path.exists(self.CONFIGFILE):
            self.save("8888888888", "2", "9", 0)
        else:
            pass

    def item(self, key: str):
        '''解析配置文件'''
        with open(self.CONFIGFILE, "r", encoding="utf-8") as fp:
            doc = load(fp)
        return doc.item(key)
    
    def save(self, qq: str, interval: str, number: str, loginmode: int | None):
        '''保存配置文件'''
        doc = document()

        doc.add(comment("autozan config file"))
        doc.add(comment("© 2025 by XShaw201"))
        doc.add(comment("https://github.com/JackShaw201/autozan"))

        doc.add("qq", qq)
        doc.add("interval", interval)
        doc.add("number", number)
        doc.add("loginmode", loginmode)

        with open(self.CONFIGFILE, "w", encoding="utf-8") as fp:
            dump(doc, fp)

if __name__ == "__main__":
    config = Config()

    root = maliang.Tk(size=(600, 400), title="QQ空间自动点赞 v0.2.2", icon="favicon.ico")
    root.center()
    root.resizable(0, 0)

    cv = maliang.Canvas(root, auto_zoom=True, auto_update=True)
    cv.place(width=800, height=600, x=0, y=0)

    # QQ号输入框
    maliang.Text(cv, (10, 30), text="QQ 号：", anchor="w")
    input1 = maliang.InputBox(cv, (90, 10), size=(140, 40))
    input1.append(config.item("qq"))

    # 密码输入框
    maliang.Text(cv, (240, 30), text="密码：", anchor="w")
    input2 = maliang.InputBox(cv, (300, 10), size=(290, 40), show="*")

    # Cookie 输入框
    maliang.Text(cv, (10, 80), text="Cookie：", anchor="w")
    input3 = maliang.InputBox(cv, (90, 60), size=(500, 40))

    # 间隔输入框
    maliang.Text(cv, (10, 130), text="间隔：", anchor="w")
    input4 = maliang.SpinBox(cv, (70, 110), size=(80, 40), default=config.item("interval"))
    maliang.Text(cv, (160, 130), text="分钟", anchor="w")

    # 条数输入框
    maliang.Text(cv, (220, 130), text="条数：", anchor="w")
    input5 = maliang.SpinBox(cv, (280, 110), size=(80, 40), default=config.item("number"))

    # 点赞统计
    text1 = maliang.Text(cv, (20, 170), text="已为您的好友献出 0 个赞\n已刷新 0 次")

    # 登录方式选择
    maliang.Text(cv, (10, 315), text="登录方式：", anchor="w")
    sb = maliang.SegmentedButton(cv, (110, 291), text=("快捷登录", "密码登录", "Cookie 登录"), default=config.item("loginmode"))

    b1 = maliang.Button(cv, (10, 350), size=(580, 40), text="开始", command=lambda: start(input1.get(), int(input4.get()), sb.get(), b2, text1))
    b2 = maliang.Button(cv, (10, 350), size=(580, 40), text="暂停", command=lambda: stop(b2))
    b2.forget()

    root.at_exit(lambda: (config.save(input1.get(), input4.get(), input5.get(), sb.get()), stop(b2)))
    root.mainloop()