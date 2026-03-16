print("=" * 50)
print("1. 文件打开和读取")
print("=" * 50)

# 写入文件
with open('test.txt','w',encoding='utf-8') as f:
    f.write('Hello,Python!\n')
    f.write('文件操作练习\n')
    f.write('这是第三行\n')

print("文件写入完成")

# 读取整个文件
with open('test.txt','r',encoding='utf-8') as f:
    content = f.read()
    print("read()读取:")
    print(content)

# 逐行读取
print("\n逐行读取:")
with open('test.txt','r',encoding='utf-8') as f:
    for line in f:
        print(f"{line.strip()}")    # strip() 去掉换行符号

# readlines() 读取所有行
print("\n readlines()读取:")
with open('test.txt','r',encoding='utf-8') as f:
    lines = f.readlines()    # readlines()一次性读取所有行，返回列表，每行作为列表的一个元素
    print(f"文件共有{len(lines)}行")
    for i,line in enumerate(lines,1):   # enumerate()函数同时获取索引和元素值，start=1让行号从1开始计数
        print(f"第{i}行:{line.strip()}")   # strip()去除每行末尾的换行符\n和首尾空白字符

print("\n"+"=" * 50)
print("2.文件追加和写入")
print("=" * 50)

# 追加模式
with open('test.txt','a',encoding='utf-8') as f:    # 追加模式应该使用 a
    f.write('这是追加的一行\n')
    f.write('追加完成\n')

# 读取验证
with open('test.txt','r',encoding='utf-8') as f:
    print(f.read())

print("\n"+"=" * 50)
print("3.异常处理")
print("=" * 50)

# 处理文件不存在的情况
try:         # try块：尝试执行的代码，可能引发异常
    with open('not_exist.txt','r',encoding='utf-8') as f:
        print(f.read())        # 如果文件存在，读取并打印内容
except FileNotFoundError:
    # except块：捕获特定类型的异常并处理
    # 当文件不存在时，会执行这里的代码
    print("文件不存在, 已捕获异常")
except Exception as e:
    # 捕获其他所有类型的异常
    # e是异常对象，包含错误信息
    print(f"其他错误: {e}")