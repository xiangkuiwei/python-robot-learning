# 导入相关模块

import torch
from torch.utils.data import TensorDataset
from torch.utils.data import DataLoader
from torch import nn
from torch import optim
from sklearn.datasets import make_regression
import matplotlib.pyplot as plt

# Mac 上可用的中文字体设置
plt.rcParams['font.sans-serif'] = ['Arial Unicode MS', 'Heiti TC', 'STHeiti']
plt.rcParams['axes.unicode_minus'] = False

def create_dataset():
    # 1. 创建数据集对象
    x, y, coef = make_regression(
        n_samples= 100,     # 100个样本点
        n_features= 1,      # 1个特征
        noise= 10,          # 噪声 噪声越大 样本点越散
        coef=True,          # 是否返回系数 默认为False 返回值为None
        bias=14.5,          # 偏置
        random_state=3      # 随机种子
    )

    # 2. 把上述数据封装成 张量对象
    # 重点: numpy对象 -> 张量Tensor -> 数据集对象 TensorDataset -> 数据加载器 DataLoader !!!!!!!!!!!!
    x = torch.tensor(x,dtype=torch.float32)
    y = torch.tensor(y,dtype=torch.float32)

    # 3.返回结果
    return x,y,coef

# 2.定义函数 表示模型训练

def train(x,y,coef):
    # 1.创建数据集对象 把tensor -> 数据集对象 -> 数据加载器
    dataset = TensorDataset(x,y)
    # 2.创建数据加载器对象.   参数1:数据集对象  参数2:批次大小  参数3:是否打乱数据(训练集打乱,测试集不打乱)
    dataloader = DataLoader(dataset, batch_size=16, shuffle=True)  # 每批16个
    # 3.创建初始的线性回归模型   参数1:输入特征维度   参数2:输出特征维度
    model = nn.Linear(1,1)
    # 4.创建损失函数对象
    criterion = nn.MSELoss()
    # 5.创建优化器对象      参数1:模型参数       参数2:学习率
    optimizer = optim.SGD(model.parameters(),lr=0.01)
    # 6.具体的训练过程
    # 6.1 定义变量 分别表示:训练轮数 每轮的平均损失值 总损失 每轮的批次数
    epochs, loss_list, total_loss, total_sample = 100,[],0,0
    # 6.2 开始训练 按轮训练
    for epoch in range(epochs):  # epoch的值:0,1,2,...,99
        # 6.3 每轮是 分批次 训练的 所以从 数据加载器中 获取 批次数据
        for train_x, train_y in dataloader: # 7批(16,16,16,16,16,16,4)
            # 6.4 模型预测 
            y_pred = model(train_x)
            # 6.5 计算(每批的平均)损失值
            loss = criterion(y_pred,train_y.reshape(-1,1)) # -1自动计算
            # 6.6 计算总损失 和样本批次数
            total_loss += loss.item()
            total_sample += 1
            # 6.7 梯度清零 + 反向传播 + 梯度更新
            optimizer.zero_grad()  # 梯度清零
            loss.backward()        # 反向传播
            optimizer.step()       # 梯度更新
        # 6.8 把本轮的平均损失值, 添加到列表中
        loss_list.append(total_loss/total_sample)
        print(f'轮数:{epoch + 1}, 平均损失值:{total_loss/total_sample}')
    
    # 7. 打印最终的训练结果
    print(f'{epochs}轮的平均损失分别为:{loss_list}')
    print(f'模型参数, 权重:{model.weight}, 偏置:{model.bias}')

    # 8.绘制损失图像
    plt.plot(range(epochs),loss_list)
    plt.title('损失值曲线变化图')
    plt.grid()
    plt.show()

    # 9.绘制预测值和真实值的关系
    # 9.1 绘制样本点分布情况.
    plt.scatter(x,y)
    # 9.2 绘制训练模型的预测值
    # x: 100个样本点的特征
    y_pred = torch.tensor(data = [v * model.weight + model.bias for v in x])
    # 9.3 计算真实值
    y_true = torch.tensor(data = [v *coef + 14.5 for v in x])
    # 9.4 绘制图形预测值和真实值
    plt.plot(x,y_pred,color='red',label='预测值')
    plt.plot(x,y_true,color='green',label='真实值')
    # 9.5 图例 网格
    plt.legend()
    plt.grid()
    # 9.6 显示图像
    plt.show()



if __name__ == '__main__':
    x,y,coef = create_dataset()
    print(f'x:{x},y:{y},coef:{coef}')
    train(x,y,coef)

