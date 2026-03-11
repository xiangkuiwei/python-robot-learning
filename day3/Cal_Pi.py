# Cal_Pi 蒙特卡洛方法计算Pi。

from random import random
from time import perf_counter
DARTS = 1000*1000
hits = 0.0
start = perf_counter()       # 记录时间
for i in range(1,DARTS+1):
    x, y = random(), random()
    dist = pow(x**2+y**2,1/2)  # pow(x,m) x的m次方
    if dist < 1.0:
        hits = hits+1
pi = 4 * (hits/DARTS)
print("圆周率值是：{}".format(pi))
print("运行时间是：{:.5f}s".format(perf_counter()-start)) 