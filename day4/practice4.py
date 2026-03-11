# 汉诺塔递归解法
def hanoi(n, source, target, auxiliary):
    # n:盘子数量   source:源柱子   target: 目标柱子  auxiliary:辅助柱子
    if n == 1:
        print(f"移动盘子 1: {source} -> {target}")
    else:
        hanoi(n-1, source, auxiliary, target)
        print(f"移动盘子{n}: {source} -> {target}")
        hanoi(n-1, auxiliary, target, source)
print("汉诺塔递归示例(3个盘子)")
print("目标: 将盘子从A移到C")
print("-" * 30)
hanoi(3, 'A', 'C', 'B')
print("-" * 30)
print(f"最少移动次数: {2**3-1}")