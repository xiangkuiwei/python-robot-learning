"""
学习率衰减策略介绍:
目的: 交之于 AdaGrad RMSProp Adam 方式, 我们可以通过 等间隔 指定间隔 指数等方式 来手动控制学习率
分类: 等间隔学习率衰减  指定间隔学习率衰减  指数学习率衰减
等间隔学习率衰减: 
    step_size: 间隔的轮数 即多少轮调整一次学习率
    gamma: 学习率衰减系数 lr新 = lr旧 * gamma

指定间隔学习率衰减:
    milestones = [50,125,160] 指定学习率需要调整的轮数
    gamma: 学习率衰减系数 lr新 = lr旧 * gamma ** epoch
"""

import torch
from torch import optim
import matplotlib.pyplot as plt

# 1.等间隔学习率衰减
def dm01():
    # 1 定义变量 记录 初始的学习率 训练的轮数 每轮训练的批次数
    lr, epochs, iteration =0.1, 200,10

    # 2. 创建数据集 y_true x w
    y_true = torch.tensor([0])
    x = torch.tensor([1.0],dtype=torch.float32)
    w = torch.tensor([1.0],requires_grad=True,dtype=torch.float32)

    # 3.创建优化器
    optimizer = optim.SGD([w], lr=lr, momentum=0.9)

    # 4.创建学习率衰减对象
    # 参数1: 优化器对象  参数2:间隔的轮数(多少轮调整一次学习率) 参数3:学习率衰减系数
    scheduler = optim.lr_scheduler.StepLR(optimizer, step_size=50, gamma=0.5)

    # 5.创建两个列表分别表示 训练轮数 每轮训练用的学习率
    lr_list, epoch_list = [], []

    # 6.循环遍历训练轮数 进行具体的训练
    for epoch in range(epochs):
        # 7.获取当前轮数 学习率 并保存到列表中
        epoch_list.append(epoch)
        lr_list.append(scheduler.get_last_lr())   # 获取学习率中最后的那个值

        # 8.循环遍历 每轮没批
        for batch in range(iteration):
            # 9.先计算预测值 然后基于损失函数计算损失:
            y_pred = w * x
            # 10.计算损失 最小二乘
            loss = (y_pred - y_true) ** 2
            # 11.梯度清零 + 反向传播 + 优化器更新参数
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()
        # 12. 更新学习率
        scheduler.step()

    # 13.打印结果
    print(f'lr_list:{lr_list}')

    # 14.可视化
    plt.plot(epoch_list,lr_list)
    plt.xlabel('Epoch')
    plt.ylabel('Learning Rate')
    plt.show()



# 2.指定间隔学习率衰减
def dm02():
    # 1 定义变量 记录 初始的学习率 训练的轮数 每轮训练的批次数
    lr, epochs, iteration =0.1, 200,10

    # 2. 创建数据集 y_true x w
    y_true = torch.tensor([0])
    x = torch.tensor([1.0],dtype=torch.float32)
    w = torch.tensor([1.0],requires_grad=True,dtype=torch.float32)

    # 3.创建优化器
    optimizer = optim.SGD([w], lr=lr, momentum=0.9)

    # 4.创建指定间隔学习率衰减
    milestones = [50, 125, 160]
    scheduler = optim.lr_scheduler.MultiStepLR(optimizer, milestones=milestones,gamma=0.5)

    # 5.创建两个列表分别表示 训练轮数 每轮训练用的学习率
    lr_list, epoch_list = [], []

    # 6.循环遍历训练轮数 进行具体的训练
    for epoch in range(epochs):
        # 7.获取当前轮数 学习率 并保存到列表中
        epoch_list.append(epoch)
        lr_list.append(scheduler.get_last_lr())   # 获取学习率中最后的那个值

        # 8.循环遍历 每轮没批
        for batch in range(iteration):
            # 9.先计算预测值 然后基于损失函数计算损失:
            y_pred = w * x
            # 10.计算损失 最小二乘
            loss = (y_pred - y_true) ** 2
            # 11.梯度清零 + 反向传播 + 优化器更新参数
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()
        # 12. 更新学习率
        scheduler.step()

    # 13.打印结果
    print(f'lr_list:{lr_list}')

    # 14.可视化
    plt.plot(epoch_list,lr_list)
    plt.xlabel('Epoch')
    plt.ylabel('Learning Rate')
    plt.show()


# 1.指数学习率衰减
def dm03():
    # 1 定义变量 记录 初始的学习率 训练的轮数 每轮训练的批次数
    lr, epochs, iteration =0.1, 200,10

    # 2. 创建数据集 y_true x w
    y_true = torch.tensor([0])
    x = torch.tensor([1.0],dtype=torch.float32)
    w = torch.tensor([1.0],requires_grad=True,dtype=torch.float32)

    # 3.创建优化器
    optimizer = optim.SGD([w], lr=lr, momentum=0.9)

    # 4.创建指数学习率衰减对象
    scheduler = optim.lr_scheduler.ExponentialLR(optimizer, gamma=0.9)

    # 5.创建两个列表分别表示 训练轮数 每轮训练用的学习率
    lr_list, epoch_list = [], []

    # 6.循环遍历训练轮数 进行具体的训练
    for epoch in range(epochs):
        # 7.获取当前轮数 学习率 并保存到列表中
        epoch_list.append(epoch)
        lr_list.append(scheduler.get_last_lr())   # 获取学习率中最后的那个值

        # 8.循环遍历 每轮没批
        for batch in range(iteration):
            # 9.先计算预测值 然后基于损失函数计算损失:
            y_pred = w * x
            # 10.计算损失 最小二乘
            loss = (y_pred - y_true) ** 2
            # 11.梯度清零 + 反向传播 + 优化器更新参数
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()
        # 12. 更新学习率
        scheduler.step()

    # 13.打印结果
    print(f'lr_list:{lr_list}')

    # 14.可视化
    plt.plot(epoch_list,lr_list)
    plt.xlabel('Epoch')
    plt.ylabel('Learning Rate')
    plt.show()



# 测试
if __name__ == '__main__':
    # dm01()
    # dm02()
    dm03()

