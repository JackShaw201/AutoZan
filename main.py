import maliang

root = maliang.Tk(size=(800, 600), title="QQ空间自动点赞")
root.center()
root.resizable(0, 0)

cv = maliang.Canvas(auto_zoom=True, auto_update=True)
cv.place(width=800, height=600, x=0, y=0)

root.mainloop()