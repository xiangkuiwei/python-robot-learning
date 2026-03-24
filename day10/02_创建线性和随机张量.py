# 导包
import torch

# 1.定义函数, 演示: 创建线性张量

def dm01():
    # 场景1: 创建指定范围的线性张量.
    # 参1:起始值, 参2: 结束值, 参3: 步长
    t1 = torch.arange(1,10,2)
    print(f't1:{t1},type:{type(t1)}')
    print('-' * 30)

    # 场景2: 创建指定范围的线性张量 -> 等差数列
    # 参1:起始值, 参2: 结束值, 参3: 元素个数
    t2 = torch.linspace(1,10,4)
    print(f't2:{t2},type:{type(t2)}')


def dm02():
    # step1: 设置随机种子
    # torch.initial_seed()  # 默认使用当前系统的时间戳作为随即种子
    torch.manual_seed(3)    # 设置随机种子

    # step2: 创建随机张量
    # 场景1: 均匀分布的随机张量
    t1 = torch.rand(size=(2,3))
    print(f't1:{t1},type:{type(t1)}')
    print('-' * 30)

    # 场景2: 符合正态分布的随机张量
    t2 = torch.randn(size=(2,3))
    print(f't2:{t2},type:{type(t2)}')
    print('-' * 30)

     # 场景3: 创建随机整数张量
    t3 = torch.randint(low=1, high=10, size=(2,3))
    print(f't3:{t3},type:{type(t3)}')



if __name__ == '__main__':
    # dm01()
    dm02()