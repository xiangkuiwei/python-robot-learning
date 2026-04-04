"""
演示CNN 图像分类案例
步骤:
    1.准备数据集
    2.搭建神经网络
    3.模型训练
    4.模型预测
卷积层:
    提取图像的局部特征 特征图 计算方式: N = (W - F + 2P)//S +1
    每个卷积核都是1个神经元
池化层:
    降维 有最大池化 和 平均池化
    池化只在HW上做调整 通道上不改变
"""

# 导包
import torch
import torch.nn as nn
from torchvision.datasets import CIFAR10
from torchvision.transforms import ToTensor
import torch.optim as optim
from torch.utils.data import DataLoader
import time
import matplotlib.pyplot as plt
from torchsummary import summary

# 每批次样本数
BATCH_SIZE = 8

# 1.数据集准备
def create_dataset():
    # 1.获取训练集
    # 参1:数据集路径 参2:是否是训练集 参3:数据预处理 -> 张量数据 参4: 是否联网下载
    train_dataset = CIFAR10(root='./data',train=True,transform=ToTensor(),download=True)
    # 2.获取测试集
    test_dataset = CIFAR10(root='./data',train=False,transform=ToTensor(),download=True)
    # 3.返回数据集
    return train_dataset,test_dataset

# 2.搭建卷积神经网络
class ImageModel(nn.Module):
    # 1.初始化父类成员 并 搭建神经网络
    def __init__(self):
        # 1.1初始化父类成员
        super().__init__()
        # 1.2 搭建神经网络
        # 第1个卷积层 输入3通道 输出6通道 卷积核大小3*3 步长1 填充0
        self.conv1 = nn.Conv2d(3,6,3,1,0)
        # 第一个池化层 窗口大小2*2 步长2 填充0
        self.pool1 = nn.MaxPool2d(2,2,0)
        self.conv2 = nn.Conv2d(6,16,3,1,0)
        self.pool2 = nn.MaxPool2d(2,2,0)

        # 全连接层
        self.linear1 = nn.Linear(576,120)
        self.linear2 = nn.Linear(120,84)
        self.output = nn.Linear(84,10)
    
    # 定义前向传播
    def forward(self,x):
        # 卷积层+激活函数+池化
        x = self.pool1(torch.relu(self.conv1(x)))
        x = self.pool2(torch.relu(self.conv2(x)))
        # 细节 全连接层只能处理2维数据 所以要将数据拉平
        # 参数1:样本数(行数) 参数2:列数 -1表示自动计算
        x = x.reshape(x.size(0),-1)
        # print(f'x.shape:{x.shape}')

        x = torch.relu(self.linear1(x))
        x = torch.relu(self.linear2(x))
        return self.output(x)

# 3.模型训练
def train(train_dataset):
    # 1.创建数据加载器
    dataloader = DataLoader(train_dataset,batch_size=BATCH_SIZE,shuffle=True)
    # 2.创建模型对象
    model = ImageModel()
    # 3.创建损失函数对象
    criterion = nn.CrossEntropyLoss()
    # 4.创建优化器对象
    optimizer = optim.Adam(model.parameters(),lr=1e-3)
    # 5.循环遍历epoch 开始每轮的训练动作
    #  5.1 定义变量 记录总的训练轮数
    epochs = 10 
    # 5.2 遍历 完成每轮的所有批次的训练动作
    for epoch_idx in range(epochs):
        # 5.2.1 定义变量 记录 总损失 总样本数据量 预测正确样本个数 训练开始时间
        total_loss,total_samples,total_correct,start = 0.0,0,0,time.time()
        # 5.2.2 每批训练
        for x,y in dataloader:
            # 5.2.3 切换训练模式
            model.train()
            # 5.2.4 模型预测
            y_pred = model(x)
            # 5.2.5 计算损失
            loss = criterion(y_pred,y)
            # 5.2.6 梯度清零+反向传播+参数更新
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()
            # 5.2.7 统计正确的样本个数
            # print(torch.argmax(y_pred,dim=-1)) # -1 表示行
            # print(y)
            # print(torch.argmax(y_pred,dim=-1)==y)
            # print((torch.argmax(y_pred,dim=-1)==y).sum())
            total_correct += (torch.argmax(y_pred,dim=-1) == y).sum()
            # 5.2.8
            total_loss += loss.item()*len(y)
            total_samples += len(y)
        # 走到这里说明一轮已经训练完毕
        print(f'epoch:{epoch_idx+1},loss:{total_loss/total_samples:.5f},acc:{total_correct/total_samples:.2f},time:{time.time()-start:.2f}s')
    # 6. 保存模型
    torch.save(model.state_dict(),'./model/image_model.pth')


# 4.模型测试
def evaluate(test_dataset):
    # 1.创建测试集 数据加载器
    dataloader = DataLoader(test_dataset,batch_size=BATCH_SIZE,shuffle=False)
    # 2.创建模型对象
    model = ImageModel()
    # 3.加载数据模型
    model.load_state_dict(torch.load('./model/image_model.pth'))
    # 4.定义变量统计量 预测正确的个数和总样本个数
    total_correct,total_samples = 0,0
    # 5.遍历数据加载器 获取每批数据
    for x,y in dataloader:
        # 5.1 切换模型模式
        model.eval()
        # 5.2 模型预测
        y_pred = model(x)
        # 5.3 训练时使用了crossentropyloss 所以搭建神经网络时没有加softmax激活函数 这里要用argmax
        y_pred = torch.argmax(y_pred,dim=-1) # -1表示行
        # 5.4 统计正确的样本个数
        total_correct += (y_pred == y).sum()
        # 5.5 统计总样本个数
        total_samples += len(y)
    print(f'Acc:{total_correct/total_samples:.2f}')




# 5.测试
if __name__ =='__main__':
    # 1.获取数据集
    train_dataset, test_dataset = create_dataset()
    # print(f'训练集:{train_dataset.data.shape}')
    # print(f'测试集:{test_dataset.data.shape}')
    # print(f'数据集类别:{train_dataset.class_to_idx}')

    # 图像展示
    # plt.figure(figsize=(2,2))
    # plt.imshow(train_dataset.data[11])
    # plt.title(train_dataset.targets[11])
    # plt.show()

    # 2.搭建神经网络
    # model = ImageModel()
    # 查看模型参数 参1:模型 参2:输入维度(CHW) 参数3:批次大小
    # summary(model,(3,32,32),batch_size=BATCH_SIZE)

    # 3.训练模型
    # train(train_dataset)

    # 4.模型测试
    evaluate(test_dataset)