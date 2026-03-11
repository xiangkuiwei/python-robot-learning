# 斐波那契数列
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)
print("斐波那契递归数列示例:")
for i in range(10):
    print(f"fib({i}) = {fibonacci(i)}")

# 引入计数
count = 0
def fib_count(n):
    global count
    count += 1
    if n <= 1:
        return n
    return fib_count(n-1)+fib_count(n-2)

print(f"\n fib(10) 递归函数调用次数:{count}")   
fib_count(10)
print(f"fib(10) 递归函数调用次数:{count}")