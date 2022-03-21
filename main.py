import numpy as np
from timeit import default_timer as timer
Nv = 0
Nw = 0
Bv = 0
Bw = 0

 # 贪心算法（选取价值最大的）
def GreedyAlgo(item,c,num):
    data = np.array(item)
    idex = np.lexsort([data[:,0], -1*data[:,1]])
    status = [0] * num
    Tw=0
    Tv=0

    for i in range(num):
        if data[idex[i],0] <= c:
            Tw += data[idex[i],0]
            Tv += data[idex[i],1]
            status[idex[i]] = 1
            c -= data[idex[i],0]
        else:
            continue

    print("贪心算法，最大价值为：")
    return Tv


def Dp(w,v,c,num):
    cnt=[0 for j in range(c + 1)]

    for i in range(1,num+1):
        for j in range(c,0,-1):
                if j>=w[i-2]:
                    cnt[j] =max(cnt[j],cnt[j-w[i-2]]+v[i-2] )
                
    print("动态规划算法，最大价值为：")
    return cnt[c]


def Backtracking(k,c,num):
    global Nw,Nv,Bv,Bw
    status = [0 for i in range(num)]

    if k>=num:
        if Bv<Nv:
                Bv = Nv
    else:
        if Nw + w[k] <= c:
            status[k] = 1
            Nw += w[k]
            Nv += v[k]
            Backtracking(k+1,c,num)
            Nw -= w[k]
            Nv -= v[k]
        status[k] = 0
        Backtracking(k+1,c,num)


if __name__ == '__main__':

    # 读取数据(第一行不读取)
    f = open("D:\Python_work\dp\测试数据\\beibao0.in", "r")
    a = []
    a1 = []
    res = f.readlines()[1:]

    for line in res:
        line = line.replace('\n', '')  # 去掉\n;
        line = line.split(' ')  # 以空格划分
        a.append(line)

    f.close()
    # print(a)

    # 读取数据(第一行读取)
    f1 = open("D:\Python_work\dp\测试数据\\beibao0.in", "r")
    a1 = []
    res1 = f1.readlines()

    for line in res1:
        line = line.replace('\n', '')  # 去掉\n;
        line = line.split(' ')  # 以空格划分
        a1.append(line)

    f.close()
    # print(a1)
    # 求容量重量和价值
    c = int(a1[0][0])
    num = int(a1[0][1])

    a =np.array(a)
    a=a.astype(int)
    w = (a[:, 0])
    v = (a[:, 1])
    w =np.array(w)
    v =np.array(v)
    w = w.astype(int)
    v = v.astype(int)
    item = list(zip(w,v))
    # w.sort()
    # w=abs(np.sort(-w))
    #print(w[1])
    # print(w)
    # print(v)
    # print(c)
    # print(num)
    # print(item)
    print("beibao0.in:")
    print("1：贪心算法，2：动态规划，3：回溯算法")
    while 1:
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
            file = open('D:\Python_work\dp\\resultG.txt', 'w')
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
            file = open('D:\Python_work\dp\\resultD.txt', 'w')
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
            file = open('D:\Python_work\dp\\resultB.txt', 'w')
            file.write(result)
            file.close()



