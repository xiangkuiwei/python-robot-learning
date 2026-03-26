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

# 1.创建画布和坐标轴 1行2列
fig, axes = plt.subplots(1,2)

# 2.生成-20到20之间的1000个数据点
x = torch.linspace(-20,20,1000)

# 3.计算上述1000个点 Tanh 激活函数处理
y = torch.tanh(x)

# 4.在第一个子图中绘制Tanh激活函数图像
axes[0].plot(x,y)
axes[0].set_title('Tanh激活函数图像')
axes[0].grid()

# 5.在第二个图上 绘制Tanh激活函数的导数图像
x = torch.linspace(-20,20,1000,requires_grad=True)

torch.tanh(x).sum().backward()
# 一个张量一旦设置了自动微分 这个张量就不能直接转成numpy的ndarray对象了 需要使用detach函数
axes[1].plot(x.detach(),x.grad)
axes[1].set_title('Tanh激活函数导数图像')
axes[1].grid()
plt.show()