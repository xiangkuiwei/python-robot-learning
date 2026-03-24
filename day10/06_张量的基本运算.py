import torch

# 1.创建张量
t1 = torch.tensor([1,2,3,4,5])

# 2.演示加法
# t2 = t1 + 100
# t2 =t1.add(100)
# t3 =t1.add_(100)

# 演示其他的
t2 = t1.sub(1)
t3 = t1.mul(2)
t4 = t1.div(2)
t5 = t1.neg()

# 3.打印结果
print(f't1:{t1}')
print(f't2:{t2}')
print(f't3:{t3}')
print(f't4:{t4}')
print(f't5:{t5}')