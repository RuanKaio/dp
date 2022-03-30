
import numpy as np
import matplotlib as mpl
from timeit import default_timer as timer

from matplotlib import pyplot as plt

Nv = 0
Nw = 0
Bv = 0
Bw = 0


# 贪心算法（选取价值最大的）
def GreedyAlgo(item, c, num):
    data = np.array(item)
    idex = np.lexsort([data[:, 0], -1 * data[:, 1]])
    status = [0] * num
    Tw = 0
    Tv = 0

    for i in range(num):
        if data[idex[i], 0] <= c:
            Tw += data[idex[i], 0]
            Tv += data[idex[i], 1]
            status[idex[i]] = 1
            c -= data[idex[i], 0]
        else:
            continue

    print("贪心算法，最大价值为：")
    return Tv


# 动态规划算法

def Dp(w, v, c, num):
    cnt = [0 for j in range(c + 1)]

    for i in range(1, num + 1):
        for j in range(c, 0, -1):
            if j >= w[i - 2]:
                cnt[j] = max(cnt[j], cnt[j - w[i - 2]] + v[i - 2])

    print("动态规划算法，最大价值为：")
    return cnt[c]


# 回溯法

def Backtracking(k, c, num):
    global Nw, Nv, Bv, Bw
    status = [0 for i in range(num)]

    if k >= num:
        if Bv < Nv:
            Bv = Nv
    else:
        if Nw + w[k] <= c:
            status[k] = 1
            Nw += w[k]
            Nv += v[k]
            Backtracking(k + 1, c, num)
            Nw -= w[k]
            Nv -= v[k]
        status[k] = 0
        Backtracking(k + 1, c, num)


if __name__ == '__main__':

    print("从给定文件列表中选择测试数据：\n 0 beibao0.in\n 1 beibao1.in\n 2 beibao2.in\n 3 beibao3.in")
    print(" 4 beibao4.in\n 5 beibao5.in\n 6 beibao6.in\n 7 beibao7.in\n 8 beibao8.in\n 9 beibao9.in\n ")
    filename = input("输入文件名:")

    # 读取数据(第一行不读取)
    f = open("测试数据/" + filename, 'r')

    a = []
    a1 = []
    res = f.readlines()[1:]

    for line in res:
        line = line.replace('\n', '')  # 去掉\n;
        line = line.split(' ')  # 以空格划分
        a.append(line)

    # f.close()
    # print(a)

    # 读取数据(第一行读取)
    f1 = open("测试数据/" + filename, 'r')
    a1 = []
    res1 = f1.readlines()

    for line in res1:
        line = line.replace('\n', '')  # 去掉\n;
        line = line.split(' ')  # 以空格划分
        a1.append(line)

    # f.close()
    # print(a1)
    # 求容量重量和价值
    c = int(a1[0][0])
    num = int(a1[0][1])

    a = np.array(a)
    a = a.astype(int)
    w = (a[:, 0])
    v = (a[:, 1])
    w = np.array(w)
    v = np.array(v)
    w = w.astype(int)
    v = v.astype(int)
    item = list(zip(w, v))
    # w.sort()
    # w=abs(np.sort(-w))
    # print(w[1])
    # print(w)
    # print(v)
    # print(c)
    # print(num)
    # print(item)
    print("\n打开的文件为: " + filename + "; 数据如下：")
    print(item)
    while 1:
        print("请选择操作：\n1. 使用算法求解\n2. 画散点图\n3. 排序\n4.退出")
        choose = int(input())
        if choose == 1:
            print("1：贪心算法，2：动态规划，3：回溯算法")

            msg = int(input())
            if msg == 1:
                time_start = timer()

                ret1 = GreedyAlgo(item, c, num)
                print(ret1)

                time_end = timer()
                time_sum = time_end - time_start
                print("求解时间为：")
                print(time_sum)

                result = "贪心算法：最优解：" + str(ret1) + "，" + "求解时间：" + str(time_sum)
                file = open('resultG.txt', 'w')
                file.write(result)
                file.close()
            elif msg == 2:
                time_start = timer()

                ret2 = Dp(w, v, c, num)
                print(ret2)

                time_end = timer()
                time_sum = time_end - time_start
                print("求解时间为：")
                print(time_sum)

                result = "动态规划算法：最优解：" + str(ret2) + "，" + "求解时间：" + str(time_sum)
                file = open('resultB.txt', 'w')
                file.write(result)
                file.close()
            else:
                time_start = timer()

                Backtracking(0, c, num)

                print("回溯算法，最大价值为：")
                print(Bv)
                time_end = timer()
                time_sum = time_end - time_start
                print("求解时间为：")
                print(time_sum)

                result = "回溯算法：最优解：" + str(Bv) + "，" + "求解时间：" + str(time_sum)
                file = open('resultB.txt', 'w')
                file.write(result)
                file.close()
        elif choose == 2:
            mpl.rcParams['font.family'] = 'sans-serif'
            mpl.rcParams['font.sans-serif'] = 'NSimSun,Times New Roman'

            # res = f.readlines()[1:]
            x, y = np.loadtxt(res, delimiter=' ', unpack=True)
            plt.plot(x, y, '.', color='blue')

            plt.xlabel('wight')
            plt.ylabel('value')
            plt.title('scatter plot')
            plt.legend()
            plt.show()
        elif choose == 3:
            # 计算重量与价值的比值
            F0 = int(a[0][0])
            S0 = int(a[0][1])
            T0 = F0 / S0
            F1 = int(a[1][0])
            S1 = int(a[1][1])
            T1 = F1 / S1
            F2 = int(a[2][0])
            S2 = int(a[2][1])
            T2 = F2 / S2
            F3 = int(a[3][0])
            S3 = int(a[3][1])
            T3 = F3 / S3
            F4 = int(a[4][0])
            S4 = int(a[4][1])
            T4 = F4 / S4
            descending = [T0, T1, T2, T3, T4]
            print("非递增排序前为：")
            print(descending)
            descending.sort(reverse=True)
            print("非递增排序后为：")
            print(descending)
        elif choose == 4:
            exit()
