from IPython.core.interactiveshell import InteractiveShell
import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
# 定义拟合函数
def func(x, a, b, c):
    return a * x ** 2 + b * x + c
data = np.loadtxt('data.txt')
# 实验数据 
#x = [1, 2, 3, 4, 5]
#y = [1, 1, 6, 10, 15]
# 实验数据 
x = data[:, 0]  
y = data[:, 1]

# 调用curve_fit进行拟合
popt, pcov = curve_fit(func, x, y)

# 打印拟合参数
print(popt)
# [ 1.  2.  1.]

# 绘制拟合曲线
x1 = np.linspace(0, 6, 100)
y1 = func(x1, popt[0], popt[1], popt[2])


plt.plot(x1, y1, 'r-', label='fit')
plt.plot(x, y, 'o', label='data')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()

