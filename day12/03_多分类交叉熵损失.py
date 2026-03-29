"""
多分类交叉熵损失: CrossEntropyLoss
    设计思路: 
             Loss = - \sigma ylog(S(f(x)))
             x:样本
             f(x):加权求和
             S(f(x)): 处理后的概率 
             y: 样本 x 属于某一个类别的 真实概率
    CrossEntropyLoss = Softmax()+损失计算，
    后续如果用这个损失函数，则：输出层就不用额外调用 softmax()激活函数了.
"""

import torch
import torch.nn as nn

# 1.定义函数 演示 多分类交叉熵损失

def dm01():
    # 1.手动创建真实样本
    # y_true = torch.tensor([[0,1,0],[1,0,0]])
    y_true = torch.tensor([1,2])

    # 2.手动创建样本的预测值 就是公式中的 f(x)
    y_pred = torch.tensor([[0.1,0.8,0.1],[0.7,0.2,0.1]],requires_grad=True,dtype=torch.float)

    # 3.创建多分类交叉熵损失函数
    criterion = nn.CrossEntropyLoss()

    # 4.计算损失值
    loss = criterion(y_pred,y_true)
    print(f'损失值:{loss}')

if __name__ == '__main__':
    dm01()