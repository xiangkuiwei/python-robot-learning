# for 循环基础
print("1. for 循环:")
for i in range(10):
    print(f"i={i}")
    print(i)
    print("i")

# range 的各种用法
print("\n 2. range 用法:")
print(range(1,8))
print({range(1,8)})
print(list(range(1,9)))
print("range(1,8):",list(range(1,8)))     # list 用法   
print("range(1,10,2):",list(range(1,10,2)))
print("range(5,0,-1):",list(range(5,0,-1)))

# 3. while 循环
print("\n 3. while循环:")
count = 0
while count < 5:
    print(f"count = {count}")
    count +=1

# 4. 列表推导式
print("\n 4. 列表推导式:")
squares = [x**2 for x in range(10)]        # for...in... 的用法
print(f"squares = {squares}")

# 5. 带条件的列表推导式
even_squares = [x**2 for x in range(10) if x % 2 == 0]     # for...in...if... 的用法
print(f"even_squares = {even_squares}")

# 6.函数定义
print("\n 5. 函数定义:")
def greet(name):
    return f"hello,{name}!"
print(f"greet('robot') = {greet('robot')}")

def add(a,b):
    return a+b
print(f"add(3,5)={add(3,5)}")

# 7. break 和 continue
for c in "PYTHON":
    if c == "T":    # T 需要加引号 "T" 
        continue
    print(c,end=" ")
print()

for m in "PYTHON":
    if m == "T":    # T 需要加引号 "T"
        break
    print(m,end=" ")
print()

s = "PYTHON"
while s != "":
    for c in s:
        print(c,end="")
    s = s[:-1]             # 去掉最后一个字符 
print()

s = "PYTHON"
while s != "":
    for c in s:
        if c == "T":
            break
        print(c,end="")
    s = s[:-1]            # 去掉最后一个字符  
print()

# 8. 循环与else
for c in "PYTHON":
    if c == "T":
        continue           # 跳过当前循环，继续下一次。
    print(c, end="")
else:
    print("正常退出")

for c in "PYTHON":
    if c == "T":
        break               # break 导致循环提前终止, 不会执行else板块。
    print(c, end="")
else:
    print("正常退出")