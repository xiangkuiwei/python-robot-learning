import torch
# 1.定义函数，演示 张量点乘
def dmo1():
    # 创建两个张量
    t1 = torch.tensor([[1,2,3],[4,5,6]])
    t2 = torch.tensor([[9,8,7],[6,5,4]])
    print(f't1:{t1}')
    print(f't2:{t2}')

    # 进行点乘运算
    t3 = t1 * t2
    t4 =t1.mul(t2)
    print(f't3:{t3}')
    print(f't4:{t4}')

# 2.定义函数，演示 张量矩阵乘法
def dm02():
    # 创建两个张量
    t5 = torch.tensor([[1,2,3],[4,5,6]])
    t6 = torch.tensor([[9,8],[7,6],[5,4]])  
    print(f't5:{t5}')
    print(f't6:{t6}')

    # 进行矩阵乘法
    t7 = t5 @ t6
    t8 = t5.matmul(t6)
    print(f't7:{t7}')
    print(f't8:{t8}')

# 3.演示 dot 函数, 仅对一维张量有效
def dm03():
    t9 = torch.tensor([1,2,3])
    t10 = torch.tensor([4,5,6])
    t11 = t9.dot(t10)
    print(f't11:{t11}')

if __name__ == '__main__':
    # dmo1()
    # dm02()
    dm03()

