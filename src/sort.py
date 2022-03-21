import numpy
#能够对一组{0-1}KP数据按重量比进行非递增排序

if __name__ == '__main__':
    #读取数据
    f=open("D:\Python_work\dp\测试数据\\beibao0.in","r")
    a=[]
    res=f.readlines()[1:]
    for line in res:
        line=line.replace('\n','')      #去掉\n;
        line=line.split(' ')        #以空格划分
        a.append(line)

    f.close()
    print("从beibao0.in文件中读取的数据为：")
    print(a)

    #计算重量与价值的比值
    F0=int(a[0][0])
    S0=int(a[0][1])
    T0=F0/S0
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
    descending=[T0,T1,T2,T3,T4]
    print("非递增排序前为：")
    print(descending)
    descending.sort(reverse=True)
    print("非递增排序后为：")
    print(descending)
