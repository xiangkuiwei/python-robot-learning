# 1.字符串索引。
s = "robot"
print(f"s={s}")
print(f"s[0]={s[0]}")
print(f"s[-1]={s[-1]}")
print(f"s[1:4]={s[1:4]}")
# 索引操作本身：只需要用[]，不需要 {}。
# f-string 中：需要用{}包裹任何想要计算的表达式，包括索引操作。
print(s)
print(s[0])
print(s[-1])
print(s[1:4])

# 2.split()方法
data = "j1:1.57,j2:0.78,j3:-1.2"
parts = data.split(",")
print(f"split结果:{parts}")

# 3.进一步分割
print("\n逐对解析:")
for part in parts:
    joint, angle = part.split(":")
    print(f" 关节: {joint}, 角度: {angle} ")

# 4.strip() 去除空格
s2 = "  hello robot  "
print(f"\n带空格:'{s2}'")
print(f"strip后:'{s2.strip()}'")

# 5. 列表操作
angles = [1.57,0.78,-1.2]
print(f"\n角度列表: {angles}")
print(f"最大角度: {max(angles)}")
print(f"最小角度: {min(angles)}")
print(f"平均角度: {sum(angles)/len(angles):.2f}")