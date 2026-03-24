import torch

# 1.定义张量, 记录处值
t1 = torch.tensor([
    [1,2,3],
    [4,5,6] 
],dtype=torch.float)
print(f't1:{t1}')

# 2. 演示 有dim参数的 函数
# sum() 求和
t2 = t1.sum()        # 整体求和  
t3 = t1.sum(dim=0)   # dim=0 按 列 求和 
t4 = t1.sum(dim=1)   # dim=1 按 行 求和
print(f't2:{t2}')
print(f't3:{t3}')
print(f't4:{t4}')
print('-' * 30)

# max()
t5 = t1.max()   
t6 = t1.max(dim=0)    # 按 列 求最大值
t7 = t1.max(dim=1)    # 按 行 求最大值
print(f't5:{t5}')
print(f't6:{t6}')
print(f't7:{t7}')
print('-' * 30)

# mean()
print(t1.mean())
print(t1.mean(dim=0))
print(t1.mean(dim=1))
print('-' * 30)

# 3. 演示 无dim参数的 函数  
# pow() 幂次
print(t1.pow(2))
print(t1.pow(3))
print(t1 ** 3)
print('-' * 30)

# sqrt() 平方根
print(t1.sqrt())
print('-' * 30)

# exp() e的n次幂
print(t1.exp())
print('-' * 30)

# log() log2() log10()
print(t1.log())
print(t1.log2())
print(t1.log10())