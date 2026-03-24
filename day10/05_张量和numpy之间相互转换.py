import torch
import numpy as np

# 1.定义函数, 演示:张量->numpy
def dm1():
    # 1,1 创建张量
    t1 = torch.tensor([1,2,3,4,5])
    print(f't1:{t1},type:{type(t1)}')
    print('-' * 30)

    # 1.2 张量 -> numpy
    # n1 = t1.numpy()       # 共享内存
    n1 = t1.numpy().copy()  # 不共享内存
    print(f'n1:{n1},type:{type(n1)}')

    # 1.3 测试是否共享内存
    n1[0] = 100
    print(f'n1:{n1}')
    print(f't1:{t1}')

# 2.定义函数, 演示:numpy->张量
def dm2():
    # 2.1 创建numpy数组
    n1 = np.array([1,2,3,4,5])
    print(f'n1:{n1},type:{type(n1)}')

    # 2.2 numpy -> 张量
    # t1 = torch.from_numpy(n1)           # 共享内存 
    t1 = torch.tensor(n1)                 # 不共享内存
    print(f't1:{t1},type:{type(t1)}')

    # 2.3 测试是否共享内存
    t1[0] = 100
    print(f't1:{t1}')
    print(f'n1:{n1}')

# 3.定义函数, 演示:从标量张量(只有1个值的张量)中 提取内容

def dm3():
    # 3.1 创建标量张量
    t1 = torch.tensor(5)           # 可以
    # t1 = torch.tensor([5, ])     # 可以
    # t1 = torch.tensor([4,6])     # 不可以
    print(f't1:{t1},type:{type(t1)}')

    # 3.2 从标量张量中 提取内容
    a = t1.item()
    print(f'value:{a},type:{type(a)}')



if __name__ == '__main__':
    # dm1()
    # dm2()
    dm3()