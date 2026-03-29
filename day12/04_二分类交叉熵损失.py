"""
二分类交叉熵损失: Loss = -ylog(预测值) - (1-y)log(1-预测值)
               由于公式中没有sigmoid激活函数 使用BCELoss的时候 还需要手动指定Sigmoid
"""

import torch
import torch.nn as nn

# 1.定义函数 演示 二类交叉熵损失

def dm01():
    # 1.设置真实值
    y_true = torch.tensor([0,1,0],dtype=torch.float)

    # 2.设置预测值
    y_pred = torch.tensor([0.6901,0.1111,0.2345])

    # 3.创建多分类交叉熵损失函数
    criterion = nn.BCELoss()

    # 4.计算损失值
    loss = criterion(y_pred,y_true)
    print(f'损失值:{loss}')

if __name__ == '__main__':
    dm01()