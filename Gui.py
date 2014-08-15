from tkinter import *
# import tkinter.filedialog

def test():
    print('hello world!')

def display():
	var.set(var.get()+'\n!!!!!')

win = Tk()  #定义一个窗体
win.title('Hello World')    #定义窗体标题
win.geometry('400x300')     #定义窗体的大小，是400X200像素
btn1 = Button(win, text='Click me', command=display)
btn2 = Button(win, text='Click you', command=display)
var = StringVar()
var.set("wtfd!")
lo = Label(win,textvariable=var,width=100)
lo.pack()
#注意这个地方，不要写成hello(),如果是hello()的话，
#会在mainloop中调用hello函数，
# 而不是单击button按钮时出发事件
btn1.pack(expand=1, fill='none') #将按钮pack，充满整个窗体(只有pack的组件实例才能显示)
btn2.pack(expand=1, fill='none')
mainloop() #进入主循环，程序运行