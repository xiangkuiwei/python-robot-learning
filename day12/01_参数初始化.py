"""
参数初始化: 
    无法打破对称性: 全0 全1 固定值
    可打破对称性的: 随机初始化 正态分布初始化 kaiming初始化 xavier初始化

重点掌握: 
    1.kaiming初始化 Xavier初始化 全0初始化
    2.关于初始化的选择上: 
          激活函数ReLU及其系列: 优先用kaiming初始化
          激活函数非ReLU: 优先用xavier
          如果是浅层网络:可以考虑使用 随机初始化
"""

import torch
import torch.nn as nn

# 1.均匀分布初始化
def dm01():
    # 1.创建1个线性层 输入维度5 输出维度3
    linear = nn.Linear(5,3)
    # 2. 对权重w进行初始化 从0-1均匀分布中产生参数
    nn.init.uniform_(linear.weight)
    # 3. 对偏置b进行随机初始化 从0-1均匀分布产生参数
    nn.init.uniform_(linear.bias)
    # 4.打印生成结果
    print(linear.weight.data)
    print(linear.bias.data)


# 2.固定初始化
def dm02():
    # 1.创建1个线性层 输入维度5 输出维度3
    linear = nn.Linear(5,3)
    # 2. 对权重w进行初始化 固定初始值
    nn.init.constant_(linear.weight,3)
    # 3. 对偏置b进行 固定初始值
    nn.init.constant_(linear.bias,3)
    # 4.打印生成结果
    print(linear.weight.data)
    print(linear.bias.data)

# 3. 全0初始化
def dm03():
    # 1.创建1个线性层 输入维度5 输出维度3
    linear = nn.Linear(5,3)
    # 2. 对权重w进行全0初始化
    nn.init.zeros_(linear.weight)
    # 3. 对偏置b进行全0初始化
    nn.init.zeros_(linear.bias)
    # 4.打印生成结果
    print(linear.weight.data)
    print(linear.bias.data)

# 4. 全1初始化
def dm04():
    # 1.创建1个线性层 输入维度5 输出维度3
    linear = nn.Linear(5,3)
    # 2. 对权重w进行全1初始化
    nn.init.ones_(linear.weight)
    # 3. 对偏置b进行全1初始化
    nn.init.ones_(linear.bias)
    # 4.打印生成结果
    print(linear.weight.data)
    print(linear.bias.data)

# 5. 正态分布初始化
def dm05():
    # 1.创建1个线性层 输入维度5 输出维度3
    linear = nn.Linear(5,3)
    # 2. 对权重w进行正态分布初始化
    nn.init.normal_(linear.weight)
    # 3.打印生成结果
    print(linear.weight.data)

# 6.kaiming初始化
def dm06():
    # 1.创建1个线性层 输入维度5 输出维度3
    linear = nn.Linear(5,3)
    # 2. kaiming 正态初始化
    nn.init.kaiming_normal_(linear.weight)
    # 3.kaiming 均匀分布初始化
    # nn.init.kaiming_uniform_(linear.weight)
    # 3.打印生成结果
    print(linear.weight.data)


# 6. xavier初始化
def dm07():
    # 1.创建1个线性层 输入维度5 输出维度3
    linear = nn.Linear(5,3)
    # 2. xavier 正态初始化
    # nn.init.xavier_normal_(linear.weight)
    # 3.xavier 均匀分布初始化
    nn.init.xavier_uniform_(linear.weight)
    # 3.打印生成结果
    print(linear.weight.data)


# 测试
if __name__ == '__main__':
    # dm01()
    # dm02()
    # dm03()
    # dm04()
    # dm05()
    dm06()