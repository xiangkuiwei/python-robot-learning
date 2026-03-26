# 导包
import torch
# 1. 定义变量 记录初始权重
w = torch.tensor(10, requires_grad=True, dtype=torch.float32)

# 2.定义损失函数 loss = w**2 + 20
loss = w ** 2 + 20

# 3.利用梯度下降法, 循环迭代100求最优解
print(f'开始 权重初始值:{w}, (0.01 * w.grad):无, loss:{loss}')

# 迭代100次
for i in range(1,101):
    # 3.1 前向传播 正向计算
    loss = w ** 2 + 20

    # 3.2 梯度清零 w.grad_zero_()  梯度默认会累加 所以需要清零
    # 但是第一次计算的时候 还没有梯度值 所以w.grad = None
    if w.grad is not None:
        w.grad.zero_()

    # 3.3 反向传播
    loss.sum().backward()

    # 3.4 梯度更新
    w.data = w.data - 0.01 * w.grad

    # 3.5 打印本次 梯度更新后的 权重参数结果.
    print(f'第{i}次, 初始权重值:{w}, (0.01 * w.grad):{0.01 * w.grad}, loss:{loss}')

    # 4.打印最终结果
    print(f'最终结果 权重:{w}, 梯度:{w.grad}, loss:{loss}')