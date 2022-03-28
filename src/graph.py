# coding:utf-8
import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl

mpl.rcParams['font.family'] = 'sans-serif'
mpl.rcParams['font.sans-serif'] = 'NSimSun,Times New Roman'

f=open("测试数据/beibao3.in","r")
res=f.readlines()[1:]

x, y = np.loadtxt(res, delimiter=' ', unpack=True)
plt.plot(x, y, '.', color='blue')

plt.xlabel('wight')
plt.ylabel('value')
plt.title('scatter plot')
plt.legend()
plt.show()