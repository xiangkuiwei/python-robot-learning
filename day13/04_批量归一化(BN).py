"""
批量归一化:
    思路: 先对数据进行标准化(会丢失一些信息),然后再对数据进行 缩放(lambta) 和平移(beta) 找补回一些信息
    应用场景: CV里面使用较多
   
    BatchNorm1d: 主要应用于全连接层或者处理1维数据的网络 例如文本处理 接收形状为(N, num_features)的张量作为输入
    BatchNorm2d:主要应用于卷积神经网络 处理2维图像数据或者特征图 接收形状为(N,C,H,W)的张量作为输入
    BatchNorm3d:
"""

import torch
import torch.nn as nn

# 定义函数 处理2维数据
def dm01():
    # 1.创建图像样本数据
    # 1张图片 2个通道 3行4列(像素点)
    input_2d = torch.randn(size=(1,2,3,4))
    print(f'input_2d:{input_2d}')

    # 2.创建批量归一化层(BN层)
    # 参数1: 输入特征数 = 图片的通道数
    # 参数2: 噪声值 默认1e-5
    # 参数3: 动量值 
    # 参数4: 表示使用可学习的变换参数 对归一化后的数据进行 缩放和平移
    bn2d = nn.BatchNorm2d(num_features=2, eps=1e-5, momentum=0.1,affine=True)
    # 3.对数据进行 批量归一化处理
    output_2d = bn2d(input_2d)
    print(f'output_2d:{output_2d}')


# 一维
def dm02():
    # 1.创建样本数据
    input_1d = torch.randn(size=(2,2))
    print(f'input_1d:{input_1d}')

    # 2.创建线性层
    linear = nn.Linear(2,4)

    # 3.用线性层进行计算
    l1 = linear(input_1d)
    print(f'l1:{l1}')

    # 4. 创建批量归一化层
    bn1d = nn.BatchNorm1d(num_features=4)

    # 5. 对线性处理结果l1进行 批量归一化
    output_1d = bn1d(l1)
    print(f'output_1d:{output_1d}')

# 测试
if __name__ == '__main__':
    # dm01()
    dm02()