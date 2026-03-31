"""
案例: 基于手机的20列特征 预测手机的价格区间(4个区间)
"""

# 导包
import torch
from torch.utils.data import TensorDataset  # 数据集对象 数据 -> Tensor -> 数据集 -> 数据加载器
from torch.utils.data import DataLoader     # 数据加载器 
import torch.nn as nn
import torch.optim as optim
from sklearn.model_selection import train_test_split  # 训练集和测试集的划分
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import time
from torchsummary import summary      # 模型结构可视化
from sklearn.preprocessing import StandardScaler

# 1.定义函数 构造数据集
def create_dataset():
    # 1.加载csv文件数据集
    data = pd.read_csv('./data/手机价格预测.csv')
    # print(f'data:{data.head()}')
    # print(f'data:{data:shape}')

    # 2.获取x特征列 和 y标签列
    x, y = data.iloc[:,:-1],data.iloc[:,-1]  # 进行数据切分 

    # 3.把特征列转换为浮点型
    x = x.astype(np.float32)

    # 4.切分训练集和测试集
    # 参数1: 特征    参数2: 标签     参数3:测试集所占比例   参数4:随机种子   参数5:样本的分布(参考y的类别进行抽取数据)
    x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state=3,stratify=y)

    # 优化: 数据标准化
    transfer = StandardScaler()
    x_train = transfer.fit_transform(x_train)
    x_test = transfer.fit_transform(x_test)


    # 5 把数据集封装成 张量数据集 数据 -> 张量Tensor -> 数据集TensorDataSet -> 数据加载器DataLoader
    train_dataset = TensorDataset(torch.tensor(x_train ),torch.tensor(y_train.values))
    test_dataset = TensorDataset(torch.tensor(x_test),torch.tensor(y_test.values))

    # 6. 返回结果                         20(充当 输入特征数)   4(充当 输出标签数)
    return train_dataset, test_dataset, x_train.shape[1], len(np.unique(y))
    #  shape 返回数据的维度 0是行 1是列    np.unique 返回数组中的唯一值（去重）


# 2.搭建神经网络
class PhonePriceModel(nn.Module):
    # 1.在init魔法方法中 初始父类成员 及搭建神经网络
    def __init__(self,input_dim, output_dim):
        # 1.1 初始化父类成员
        super().__init__()
        # 1.2 搭建神经网络
        self.linear1 = nn.Linear(input_dim,128)
        self.linear2 = nn.Linear(128,512)
        self.linear3 = nn.Linear(512,256)
        self.linear4 = nn.Linear(256,128)
        self.output = nn.Linear(128,output_dim)
    
    # 2.定义前向传播方法
    def forward(self,x):
        x = torch.relu(self.linear1(x))
        x = torch.relu(self.linear2(x))
        x = torch.relu(self.linear3(x))
        x = torch.relu(self.linear4(x))
        x = self.output(x)   # 并没有使用激活函数，因为后续使用交叉熵损失函数 自带softmax
        return x
    

# 3.模型训练
def train(train_dataset,input_dim,output_dim):
    # 1 创建数据加载器 数据 -> 张量 -> 数据集 -> 数据加载器
    # 参数1:数据集对象   参数2:每批次的数据条数  参数3:是否打乱数据(训练集:打乱 测试集:不打乱)
    train_loader = DataLoader(train_dataset, batch_size=16, shuffle=True)
    # 2.创建神经网络模型
    model = PhonePriceModel(input_dim, output_dim)
    # 3.定义损失函数 
    criterion = nn.CrossEntropyLoss()
    # 4.创建优化器对象
    optimizer = optim.Adam(model.parameters(),lr=0.001)
    # 5.模型训练
    # 5.1 定义训练总轮数
    epochs = 100
    # 5.2 开始每轮训练
    for epoch in range(epochs):
        # 5.2.1 定义变量记录每轮损失值 训练批次数
        total_loss, batch_sum = 0.0, 0
        # 5.2.2 定义变量，表示训练开始的时间
        start = time.time()
        # 5.2.3 开始本轮的各批次训练
        for x, y in train_loader:
            # 切换模型状态
            model.train() # 训练模型    model.eval()
            # 模型预测
            y_pred = model(x)
            # 计算损失
            loss = criterion(y_pred,y)
            # 梯度清零 反向传播 参数优化
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()
            # 累加损失值
            total_loss += loss.item()
            batch_sum += 1
        # 5.2.4 至此 本轮训练结束 打印训练信息
        print(f'epoch:{epoch+1},loss:{total_loss/batch_sum:.4f},time:{time.time() - start:.2f}s')
    
    # 6.走到这里 说明多轮训练结束 保存模型
    torch.save(model.state_dict(),'./model/phone.pth')  # 后缀名: pth pkl pickle 均可

    
# 4.模型测试
def evaluate(test_dataset, input_dim, output_dim):
    # 1.创建神经网络
    model = PhonePriceModel(input_dim,output_dim)
    # 2.加载模型参数
    model.load_state_dict(torch.load('./model/phone.pth'))
    # 3.创建测试集的 数据加载器对象
    # 参数1: 数据集对象  参数2: 每批次的数据条数 参数3: 是否打乱数据 (测试集 不打乱)
    test_loader = DataLoader(test_dataset, batch_size=8, shuffle=False)
    # 4.定义变量 记录预测准确的样本个数
    correct = 0
    # 5.从数据加载器中 获取到每批次的数据
    for x,y in test_loader:
        # 5.1 切换模型状态 测试模式
        model.eval()
        # 5.2 模型预测
        y_pred = model(x)
        # 5.3 根据加权求和 得到类别 用argmax()获取最大值对应的下标 就是类别
        y_pred = torch.argmax(y_pred,dim=1) # dim=1 表示逐行处理
        # print(f'y_pred:{y_pred}')
        # print(f'y:{y}')

        # 5.4 统计预测正确的样本个数
        correct += (y_pred == y).sum()
    # 6.走到这里 模型预测结束 打印准确率即可
    print(f'准确率(Accuracy):{correct/len(test_dataset):.4f}')






# 测试
if __name__ == '__main__':
    # 1.准备数据集
    train_dataset,test_dataset,input_dim,output_dim = create_dataset()
    # print(f'训练集 数据集对象:{train_dataset}')
    # print(f'测试集 数据集对象:{test_dataset}')
    # print(f'输入特征数:{input_dim}')
    # print(f'输出特征数:{output_dim}')

    # 2.构建神经网络模型
    # model = PhonePriceModel(input_dim,output_dim)
    # 计算模型参数
    # summary(model, input_size=(16,input_dim))

    # 3.模型训练
    train(train_dataset,input_dim,output_dim)

    # 4.模型测试
    evaluate(test_dataset,input_dim,output_dim)

    