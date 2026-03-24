'''
涉及到的API:
    reshape()        在不改变 内容 的前提下, 修改张量的形状
    unsqueeze()      在指定的轴上增加一个(1)维度, 等价于: 升维
    squeeze()        删除所有为1的维度, 等价于:降维
    transpose()      只能交换2个维度
    permute()        可交换多个维度
    view()           只能修改连续的张量的形状 连续张量 = 内存中存储顺序 和 在张量中显示的顺序相同
    contiguous()     使不连续的张量 变成 连续张量
    is_contiguous()  判断张量是否连续
'''

import torch
# 设置随机种子
torch.manual_seed(24)
# 1.reshape 的使用
def dm01():
    # 定义2行3列的张量
    t1 = torch.randint(1,10,(2,3))
    print(f't1:{t1}, shape:{t1.shape}, row:{t1.shape[0]}, col:{t1.shape[1]},{t1.shape[-1]}')

    # 通过reshape()函数 把t1 -> 3行2列, 1行6列， 6行1列
    t2 = t1.reshape(3,2)
    t3 = t1.reshape(1,6)
    t4 = t1.reshape(6,1)
    print(f't2:{t2}, shape:{t2.shape}, row:{t2.shape[0]}, col:{t2.shape[1]},{t2.shape[-1]}')
    print(f't3:{t3}, shape:{t3.shape}, row:{t3.shape[0]}, col:{t3.shape[1]},{t3.shape[-1]}')
    print(f't4:{t4}, shape:{t4.shape}, row:{t4.shape[0]}, col:{t4.shape[1]},{t4.shape[-1]}')

# 2.unsqueeze()函数, squeeze()函数
def dm02():
    # 创建一个张量
    t1 = torch.randint(1,10,(2,3))           # (2,3)     
    print(f't1:{t1}, shape:{t1.shape}')

    # 在0维上添加一个维度
    t2 = t1.unsqueeze(0)                     # (1,2,3)
    print(f't2:{t2}, shape:{t2.shape}')

    # 在1维上添加一个维度
    t3 = t1.unsqueeze(1)                     #(2,1,3)
    print(f't3:{t3}, shape:{t3.shape}') 

    # 在2维上添加一个维度
    t4 = t1.unsqueeze(2)
    print(f't4:{t4}, shape:{t4.shape}')      #(2,3,1)

    # 删除所有为1的维度
    t5 = torch.randint(1,10,(2,1,3,1,1))
    print(f't5:{t5}, shape:{t5.shape}')
    t6 = t5.squeeze()
    print(f't6:{t6}, shape:{t6.shape}')

# 3.transpose() permute() 函数
def dm03():
    t1 = torch.randint(1,10,(2,3,4))
    print(f't1:{t1}, shape:{t1.shape}')
    print('-' * 30)

    # 改变维度 从(2,3,4)->(4,3,2)
    t2 = t1.transpose(0,2)
    t3 = t1.transpose(0,-1)
    print(f't2:{t2}, shape:{t2.shape}') 

    # 改变维度 从(2,3,4)->(4,2,3)
    t4 = t1.permute(2,0,1)
    print(f't4:{t4}, shape:{t4.shape}')

# view()函数 contiguous()函数 is_contiguous()
def dm04():
    t1 = torch.randint(1,10,(2,3))
    print(f't1:{t1}, shape:{t1.shape}')

    # 判断张量是否连续. 即: 张量中的顺序 和内存中的存储顺序是否一致
    # print(t1.is_contiguous())     # True

    # 通过 view()函数, 修改上述张量的形状
    t2 = t1.view(3,2)
    print(f't2:{t2}, shape:{t2.shape}')
    print(t2.is_contiguous())      # True

    # 通过transpose()函数 交换维度 交换后不连续了
    t3 = t1.transpose(0,1)
    print(t3.is_contiguous())      # False

    # 通过contiguous()函数, 使张量连续
    t4 = t3.contiguous()
    print(t4.is_contiguous())
    t5 = t4.view(3,2)
    print(f't5:{t5}, shape:{t5.shape}')

    


if __name__ == '__main__':
    # dm01()
    # dm02()
    # dm03()
    dm04()