"""
案例: 
     演示自动微分模块,具体如何求导数
回顾:
    权重更新公式:
        w新 = w旧 - 学习率 * 梯度
        梯度 = 损失函数的导数
    关于损失函数的导数, 无需我们手动计算, 因为非常常用, pytorch模块内置有自动微分模块,专门实现针对于 不同的损失函数求导
    结合 反向传播, 从而实现 更新权重参数w 和 偏置参数b
"""

# 导包 
import torch

# 1. 定义变量, 记录: 初始权重w
# 参数1:初始值, 参数2:是否自动微分, 参数3:数据类型
w = torch.tensor(10,requires_grad=True, dtype=torch.float)

# 2. 定义loss变量, 表示损失函数
loss = 2 * w ** 2 

# 3. 打印梯度函数类型
# print(f'梯度函数类型:{type{loss.grad_fn}}')

# 4. 计算梯度 计算完毕后, 会记录到 w.grad 属性中.
loss.sum().backward()

# 5.带入权重更新公式
w.data = w.data - 0.01 * w.grad

# 6.打印最终结果
print(f'更新后的权重:{w}')