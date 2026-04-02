"""
池化API: nn.MaxPool2d  nn.AvgPool2d
"""
# 导包
import torch
import torch.nn as nn
import matplotlib.pyplot as plt

def dm01():
    # 1.创建1个 1通道 3*3 的二维矩阵
    inputs = torch.tensor([
        [
            [0,1,2],
            [3,4,5],
            [6,7,8]
        ]
    ])

    # 2.创建最大池化层
    # 参数1:池化核(池化窗口)大小  参数2:步长  参数3:填充
    pool1 = nn.MaxPool2d(2,1,0)
    outputs = pool1(inputs)
    print(f'outputs:{outputs},shape:{outputs.shape}')

    # 3.创建平均
    pool2 = nn.AvgPool2d(2,1,0)
    outputs = pool2(inputs)
    print(f'outputs:{outputs},shape:{outputs.shape}')


def dm02():
    # 1.创建1个 3通道 3*3 的二维矩阵
    inputs = torch.tensor([
        [
            [0,1,2],
            [3,4,5],
            [6,7,8]
        ],
        [
            [10,20,30],
            [40,50,60],
            [70,80,90]
        ],
        [
            [11,22,33],
            [44,55,66],
            [77,88,99]
        ]
    ])

    # 2.创建最大池化层
    # 参数1:池化核(池化窗口)大小  参数2:步长  参数3:填充
    pool1 = nn.MaxPool2d(2,1,0)
    outputs = pool1(inputs)
    print(f'outputs:{outputs},shape:{outputs.shape}')

    # 3.创建平均
    pool2 = nn.AvgPool2d(2,1,0)
    outputs = pool2(inputs)
    print(f'outputs:{outputs},shape:{outputs.shape}')


# 测试
if __name__ == '__main__':
    # dm01()
    dm02()