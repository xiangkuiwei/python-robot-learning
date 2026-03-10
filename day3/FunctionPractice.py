# n!
def fact(n):
    s = 1
    for i in range(1, n+1):
        s *= i
    return s
print(fact(5))

# n! 增加可变参数 *b
def fact(n,*b):
    s = 1
    for i in range(1,n+1):
        s *= i
    for item in b:
        s *= item
    return s
print(fact(10,3))
print(fact(10,3,5))

# 局部变量与全局变量
n, s = 10,100     # 这里的 s 是全局变量 
def fact(n):
    s = 1         # fact()函数内部的 s 是局部变量  
    for i in range(1,n+1):
        s *= i
    return s      # 此处 s 是局部变量, 值为3628800
print(fact(n),s)  # 此处 s 是全局变量，值为100

# 局部变量转换为全局变量
n , s = 10, 100
def fact(n):
    global s                  # 使用 global 保留字，此时 s 是全局变量，100
    for i in range(1,n+1):
        s *= i
    return s                  # 此处 s 是全局变量，362880000
print(fact(n),s)              # 此处 s 是被修改后的全局变量，362880000 

# 局部变量为组合数据类型且未创建，等同于全局变量
ls = ["F","f"]
def func(a):
    ls.append(a)  #此处 ls 是列表类型，未真实创建则等同于全局变量
    return
func("c")         # 全局变量ls被修改
print(ls)

ls = ["F","f"]
def func(a):
    ls = []
    ls.append(a)  # 此处的 ls 是局部变量，['F', 'f', 'c']
    return
func("c")        
print(ls)                #此处 ls 是全局变量 ["F","f"]

# lambda函数用法
f = lambda x,y:x+y
f(10,15)
f = lambda :"lambda函数"
print(f())
