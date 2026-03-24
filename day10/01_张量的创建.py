import torch
import numpy as np

# torch.tensor(data=, dtype=, ): 根据指定数据或指定元素类型创建张量
# data: 数据
# dtype: 元素类型
def dm01():
    list1 = [[1., 2, 3], [4, 5, 6]]  # 创建的张量为 float32
    int1 = 10
    # array 默认类型是 float64，所以创建的张量为 float64
    n1 = np.array([[1., 2., 3.], [4., 5., 6.]])
    t1 = torch.tensor(data=list1)
    t2 = torch.tensor(data=int1)
    t3 = torch.tensor(data=n1)
    print('t1 的值->', t1)
    print('t1 类型->', type(t1))
    print('t2 的值->', t2)
    print('t2 类型->', type(t2))
    print('t3 的值->', t3)
    print('t3 类型->', type(t3))



# 调用函数
dm01()