"""
案例:
    演示detach()函数 解决自动微分弊端

问题: 
    一个张量一旦设置了自动微分 这个张量就不能直接转成numpy的ndarray对象了 需要使用detach函数
"""

import torch
import numpy as np

# 1.定义张量
t1 = torch.tensor([10,20], requires_grad=True, dtype=torch.float)
print(f't1:{t1}, type:{type(t1)}')

# 2.尝试把上述张量 转成 numpy 对象
# n1 = t1.numpy()         # 报错

# 3. 解决方案 通过detach()函数, 拷贝一份张量 然后再转换
t2 = t1.detach()
print(f't2:{t2},type:{type(t2)}')

# 4. 测试上述 t1 t2 是否共享一块空间 -> 共享
t1.data[0] = 100
print(f't1:{t1}, type:{type(t1)}')
print(f't2:{t2}, type:{type(t2)}')
print('-' * 30)

# 5.查看 t1 t2 谁可以自动微分
print(f't1:{t1.requires_grad}')
print(f't2:{t2.requires_grad}')
print('-' * 30)

# 6.把 t2 转换成 numpy 对象
n1 = t2.numpy()
print(f'n1:{n1},type:{type(n1)}')

# 7.最终版
n2 = t1.detach().numpy()
print(f'n1:{n2},type:{type(n2)}')
