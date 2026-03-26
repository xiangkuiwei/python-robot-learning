# 导包
import torch

# 1.定义 x 表示: 特征(输入数据), 假设: 2行5列 全1矩阵
x = torch.ones(2,5)
print(f'x:{x}')

# 2.定义 y 表示: 标签(真实值), 假设2行3列, 全1矩阵
y = torch.ones(2,3)
print(f'y:{y}')

# 3.初始化(可自动微分的权重) 和 偏置
w = torch.randn(5,3,requires_grad=True)
print(f'w:{w}')

b = torch.randn(3,requires_grad=True)
print(f'b:{b}')

# 4.前向传播 计算出 预测值z
z = torch.matmul(x,w) + b
print(f'z:{z}')

# 5.定义损失函数
criterion = torch.nn.MSELoss()
loss = criterion(z,y)
print(f'loss:{loss}')

# 6.进行自动微分 求导 结合反向传播 更新权重
loss.backward()

# 7.打印更新
print(f'w的梯度: {w.grad}')
print(f'b的梯度: {b.grad}')