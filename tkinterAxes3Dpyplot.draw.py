import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from tkinter import *
# python 3D界面上输入2个xyz坐标 绘制这两个点连接的线段
# 创建图形窗口
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# 创建 Tkinter 窗口
root = Tk()
root.title('3D 线段绘制')
root.geometry('300x200')

# 创建输入框和标签
x1_label = Label(root, text='第一个点的 x 坐标：')
x1_label.grid(row=0, column=0)
x1_entry = Entry(root)
x1_entry.grid(row=0, column=1)
y1_label = Label(root, text='第一个点的 y 坐标：')
y1_label.grid(row=1, column=0)
y1_entry = Entry(root)
y1_entry.grid(row=1, column=1)
z1_label = Label(root, text='第一个点的 z 坐标：')
z1_label.grid(row=2, column=0)
z1_entry = Entry(root)
z1_entry.grid(row=2, column=1)
x2_label = Label(root, text='第二个点的 x 坐标：')
x2_label.grid(row=3, column=0)
x2_entry = Entry(root)
x2_entry.grid(row=3, column=1)
y2_label = Label(root, text='第二个点的 y 坐标：')
y2_label.grid(row=4, column=0)
y2_entry = Entry(root)
y2_entry.grid(row=4, column=1)
z2_label = Label(root, text='第二个点的 z 坐标：')
z2_label.grid(row=5, column=0)
z2_entry = Entry(root)
z2_entry.grid(row=5, column=1)

# 创建绘制按钮


def draw_line():
    x1 = float(x1_entry.get())
    y1 = float(y1_entry.get())
    z1 = float(z1_entry.get())
    x2 = float(x2_entry.get())
    y2 = float(y2_entry.get())
    z2 = float(z2_entry.get())
    ax.clear()
    ax.plot([x1, x2], [y1, y2], [z1, z2], 'r-', linewidth=2)
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    plt.draw()
    plt.pause(0.0001)


draw_button = Button(root, text='绘制', command=draw_line)
draw_button.grid(row=6, column=0, columnspan=2)

# 显示窗口
root.mainloop()