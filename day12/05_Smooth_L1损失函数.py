"""
MAE:  平均绝对误差
     类比L1正则化 权重可以降为0 数据会变得稀疏
     弊端:在0点不平滑 可能错过最小值
MSE: 均方误差
    弊端:如果差值过大 可能会出现梯度爆破的现象

Smooth L1:
基于MAE 和MSE 做的综合 在[-1,1]里面是L2(MSE). 其他段是L1
     
"""
import torch
import torch.nn as nn

def dm01():
    # 1.定义变量 记录真实值
    y_true = torch.tensor([2.0,2.0,2.0],dtype=torch.float)

    # 2.定义变量 记录预测值
    y_pred = torch.tensor([1.0,1.0,1.9],requires_grad=True)

    # 3.创建Smooth L1损失函数对象
    criterion = nn.SmoothL1Loss()

    # 4.计算损失
    loss = criterion(y_pred,y_true)

    # 5.输出损失
    print(f'SMooth L1:{loss}')

if __name__ == "__main__":
    dm01()