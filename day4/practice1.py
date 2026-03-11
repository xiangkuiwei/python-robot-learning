# 阶乘递归示例
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
print("阶乘递归示例")
print(f"5! = {factorial(5)}")
print(f"3! = {factorial(3)}")
print(f"0! = {factorial(0)}")

# 演示递归过程
def factorial_detail(n):
    if n == 0:
        print("factorial(0) = 1")
        return 1
    else:
        print(f"factorial({n}) = {n} * factorial({n-1})")
        result = n * factorial_detail(n-1)
        print(f"factorial({n}) = {result}")
        return result
print("\n 递归过程演示：")
factorial_detail(5)
