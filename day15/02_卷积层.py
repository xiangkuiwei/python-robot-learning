"""
演示卷积层的API, 用于提取图像的局部特征 获取特征图 Feature Map
卷积神经网络:
    概述: convolutional neural network 包含卷积层的神经网络
    组成: 
        卷积层:用于提取图像的局部特征 集合卷积核实现 处理后的结果叫 特征图
        池化层:降维
        全连接层:预测结果 输出结果
    特征图的计算方式: N = (W - F + 2*P)/S + 1
    W: 输入图像的大小
    F: 卷积核的大小
    P: 填充的大小
    S: 步长
    N: 特征图大小
"""

# 导包

import torch
import torch.nn as nn
import matplotlib.pyplot as plt

# 1. 定义函数 用于完成图像的加载 卷积 特征图的可视化操作
def dm01():
    # 1.加载RGB真彩图
    img = plt.imread('./data/img.jpg')
   
    # 2.打印读到的图像信息
    # print(f'img:{img},shape:{img.shape}')  # HWC (640,640,3)
   
    # 3.把图像从 HWC 转换为 CHW, 思路:img -> 张量 -> 转换维度
    img2 = torch.tensor(img,dtype=torch.float)
    img2 = img2.permute(2,0,1)
    # print(f'img2:{img2},shape:{img2.shape}') # CHW (3,640,640)

    # 4.因为这里只有1张图 所以我们给他增加1个维度 从 CHW -> (1, C, H, W)
    img3 = img2.unsqueeze(dim=0)
    # print(f'img3:{img3},shape:{img3.shape}') # CHW -> (1,3,640,640)

    # 5.创建卷积层对象 提取特征图
    # 参数1:输入图像的通道数  参数2:输出图像的通道数(特征图的个数) 参数3:卷积核的大小  参数4:步长  参数5:填充
    conv = nn.Conv2d(3,4,3,2,0)

    # 6.具体的卷积计算
    conv_img = conv(img3)

    # 7.打印卷积后的结果
    # print(f'conv_img:{conv_img},shape:{conv_img.shape}')

    # 8 查看提取到的4个特征图
    img4 = conv_img[0]
    print(f'img4:{img4},shape:{img4.shape}')

    # 9.将上述图从 CHW 转换为 HWC
    img5 = img4.permute(1,2,0)

    # 10.可视化第1个通道的特征图
    feature1 = img5[:, :, 0].detach().numpy()
    plt.imshow(feature1)
    plt.show()



if __name__ == '__main__':
    dm01()