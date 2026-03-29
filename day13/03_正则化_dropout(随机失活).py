"""
正则化的作用: 缓解模型过拟合情况
正则化方法: 
    L1正则化: 权重可以变为0 相当于降维
    L2正则化: 权重可以无限接近0
    DropOut: 随机失活 每批次样本训练时 随机让一部分神经元死亡 防止一些特征对结果的影响较大(防止过拟合)
    BN(批量归一化):

    Dropout调用方法: nn.Dropout
"""

# 导包
import torch
import torch.nn as nn

# 1.定义函数 演示随机失活(DropOut)
def dm01():
    # 1.创建前一层隐藏层输出的结果
    t1 = torch.randint(0,10,size=(1,4)).float()

    # 2. 进行下一层 加权求和 和 激活函数计算
    # 2.1 创建全连接层
    linear1 = nn.Linear(4,5)
    # 2.2 加权求和
    l1 = linear1(t1)
    print(f'l1(加权求和后的值):{l1}')
    # 2.3 激活函数
    output = torch.relu(l1)
    print(f'output(激活函数处理后的值):{output}')

    # 3.对激活值进行随机失活dropout处理 只有训练阶段有 测试阶段没有
    # 定义随机失活函数
    dropout = nn.Dropout(p=0.4)   # 每个神经元都有40%的概率被kill
    # 具体的随机失活动作
    d1 = dropout(output) 
    print(f'd1(随机失活后的数据):{d1}')


# 测试
if __name__ == '__main__':
    dm01()