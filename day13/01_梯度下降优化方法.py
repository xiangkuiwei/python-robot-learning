"""
概述: 梯度下降是结合 本次损失函数的导数(作为梯度) 基于学习率 来更新权重的
公式: W新 = W旧 - 学习率 * (本次的)梯度
存在的问题:
    1.遇到平缓区域 梯度下降可能会慢
    2.可能会遇到鞍点(梯度为0)
    3.可能会遇到 局部极小值
解决思路:从上述的 学习率 或者 梯度入手, 进行优化, 于是有了:
        针对梯度进行修改: 动量法Momentum  
        针对学习率修改: AdaGrad RMSProp 
        综合衡量:Adam
动量法Momentum:
    公式: St = beta * St-1 + (1-beta)*Gt
    St: 本次指数移动加权平均的结构
    beta: 调节权重系数 越大 数据越平缓 历史指数移动加权平均占比越大
    St-1: 历史指数移动加权平均结果
    Gt: 本次计算出的梯度
    加入动量法后的梯度更新公式: W新 = W旧 - 学习率 * St

自适应学习率:AdaGrad
    公式: 
        累积平方梯度: St = St-1 + Gt*Gt
        St:
        St-1:
        Gt:
    学习率:
        学习率 = 学习率/(sqrt(St)+小常数)
        小常数: 1e-10  目的:防止分母变为0
    梯度下降公式:
        W新 = W旧 - 调整后的学习率 * Gt
    缺点:可能会导致学习率过早过量的降低 导致模型后期学习率太小 难以找到最优解.

自适应学习率:RMSProp 可以看做对 Adagrad做的优化 加入调和权重系数
    公式:
        指数加权平均 累积历史平方梯度:
        St = beta * St-1 + (1-bata)*Gt*Gt
        St: 累积平方梯度
        St-1: 历史累积平方梯度
        Gt: 本次的梯度
        beta: 调和权重系数
    学习率:
        学习率 = 学习率/(sqrt(St)+小常数)
    梯度下降公式:
        W新 = W旧 - 调整后的学习率 * Gt
    缺点:可能会导致学习率过早过量的降低 导致模型后期学习率太小 难以找到最优解.

自适应矩估计: Adam(Adaptive Moment Estimation)
    思路: 既优化学习率 又优化梯度
    公式: 
        一阶矩:算均值
            Mt = beta1 * Mt-1 + (1-beta1) * Gt        充当: 梯度
            St = beta2 * St-1 + (1-beta2) * Gt * Gt   充当: 学习率
        二阶矩:梯度的方差
            Mt^ = Mt/(1 - beta1^t)
            St^ = St/(1 - beta2^t)
        权重更新公式:
            W新 = W旧 - 学习率/(sqrt(St^) + 小常数) * Mt^
        
"""
import torch
import torch.nn as nn
import torch.optim as optim

# Momentum
def dm01_momentum():
    # 1.初始化权重参数
    w = torch.tensor([1.0], requires_grad=True, dtype=torch.float32)
    # 2.定义损失函数
    criterion = ((w**2)/2)
    # 3. 创建优化器 基于SGD 加入参数momentu 就是动量法
    # 参数1:(待优化的)参数列表    参数2:学习率    参数3:动量参数
    optimizer = optim.SGD(params=[w], lr=0.01, momentum=0.9)
    # 4.计算梯度值: 梯度清零 + 反向传播 + 参数更新
    optimizer.zero_grad()
    criterion.sum().backward()
    optimizer.step()
    print(f'w:{w},w.grad:{w.grad}')

    # 5.重复上述步骤 第二次 更新权重参数
    criterion = ((w**2)/2)
    optimizer.zero_grad()
    criterion.sum().backward()
    optimizer.step()
    print(f'w:{w},w.grad:{w.grad}')
# 自适应学习率(AdaGrad)
def dm02_adagrad():
    # 1.初始化权重参数
    w = torch.tensor([1.0], requires_grad=True, dtype=torch.float32)
    # 2.定义损失函数
    criterion = ((w**2)/2.0)
    # 3. 基于Adagrad(自适应学习率)
    # 参数1:(待优化的)参数列表    参数2:学习率   
    optimizer = optim.Adagrad(params=[w], lr=0.01)
    # 4.计算梯度值: 梯度清零 + 反向传播 + 参数更新
    optimizer.zero_grad()
    criterion.sum().backward()
    optimizer.step()
    print(f'w:{w},w.grad:{w.grad}')

    # 5.重复上述步骤 第二次 更新权重参数
    criterion = ((w**2)/2)
    optimizer.zero_grad()
    criterion.sum().backward()
    optimizer.step()
    print(f'w:{w},w.grad:{w.grad}')

# 自适应学习率(RMSProp)
def dm03_rmsprop():
    # 1.初始化权重参数
    w = torch.tensor([1.0], requires_grad=True, dtype=torch.float32)
    # 2.定义损失函数
    criterion = ((w**2)/2.0)
    # 3. 基于Adagrad(自适应学习率)
    # 参数1:(待优化的)参数列表    参数2:学习率   参数3: alpha
    optimizer = optim.RMSprop(params=[w], lr=0.01, alpha=0.99)
    # 4.计算梯度值: 梯度清零 + 反向传播 + 参数更新
    optimizer.zero_grad()
    criterion.sum().backward()
    optimizer.step()
    print(f'w:{w},w.grad:{w.grad}')

    # 5.重复上述步骤 第二次 更新权重参数
    criterion = ((w**2)/2)
    optimizer.zero_grad()
    criterion.sum().backward()
    optimizer.step()
    print(f'w:{w},w.grad:{w.grad}')

# 自适应矩估计Adam
def dm04_adam():
    # 1.初始化权重参数
    w = torch.tensor([1.0], requires_grad=True, dtype=torch.float32)
    # 2.定义损失函数
    criterion = ((w**2)/2.0)
    # 3. 基于Adagrad(自适应学习率)
    # betas=(梯度用的衰减系数, 学习率用的衰减系数)
    optimizer = optim.Adam(params=[w], lr=0.01, betas=(0.9,0.999)) 
    # 4.计算梯度值: 梯度清零 + 反向传播 + 参数更新
    optimizer.zero_grad()
    criterion.sum().backward()
    optimizer.step()
    print(f'w:{w},w.grad:{w.grad}')

    # 5.重复上述步骤 第二次 更新权重参数
    criterion = ((w**2)/2)
    optimizer.zero_grad()
    criterion.sum().backward()
    optimizer.step()
    print(f'w:{w},w.grad:{w.grad}')

   
# 测试
if __name__ == '__main__':
    dm01_momentum()
    dm02_adagrad()
    dm03_rmsprop()
    dm04_adam()