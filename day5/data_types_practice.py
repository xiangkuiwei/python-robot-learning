# 组合数据类型
print("=" * 50)
print("1.集合类型")
print("=" * 50)

# 集合创建
A = {1,2,3,4,5}
B = {4,5,6,7,8}
print(f"A = {A}")
print(f"B = {B}")

# 集合操作符
print(f"A & B = {A & B}")
print(f"A | B = {A | B}") 
print(f"A - B = {A - B}") 
print(f"A ^ B = {A ^ B}")

# 集合去重
data = [1,2,2,3,3,3,4,4,4,4]
unique = set(data) 
print(f"原始数据: {data}")
print(f"去重后: {unique}")
print(f"去重后转列表: {list(unique)}")

# 集合方法
C = {1,2,3}
C.add(4)
print(f"add(4)后: {C}")
C.remove(2)
print(f"remove(2)后: {C}")
# C.remove(10)  # 不存在会报错
C.discard(10)   # 不存在不会报错
print(f"discard(10)后: {C}")


print("\n" + "=" * 50)
print("2.列表类型")
print("=" * 50)

ls = [1,2,3,4,5]
print(f"ls = {ls}")
print(f"ls[0] = {ls[0]}")
print(f"ls[-1] = {ls[-1]}")
print(f"ls[1:4] = {ls[1:4]}")
print(f"ls[:3] = {ls[:3]}")
print(f"ls[3:] = {ls[3:]}")
print(f"ls[::-1] = {ls[::-1]}") # 反转 ls[::-1]

#列表操作
ls.append(6)
print(f"append(6)后: {ls}")
ls.insert(0,0)
print(f"insert(0,0)后: {ls}")
ls.pop()
print(f"pop()后: {ls}") # pop() 删掉最后一个元素
ls.pop(0)
print(f"pop(0)后: {ls}") # pop(0) 删掉第一个元素
ls.reverse()
print(f"reverse()后: {ls}") # reverse 反转
ls.sort()
print(f"sort()后: {ls}")
lp = [3,4,2,8,6]
ls
lp.sort()
print(f"sort()后: {lp}") # sort 排序 升序

# 列表推导式
squares = [x**2 for x in range(10)]
print(f"0-9的平方: {squares}")
even_squares = [x**2 for x in range(10) if x % 2 == 0]
print(f"偶数的平方: {even_squares}")

# 嵌套列表推导式
matrix = [[i*j for j in range(1,4)] for i in range(1,4)]
print(f"3*3矩阵:")
for row in matrix:
    print(f"{row}")

print("\n + '=' * 50")
print("3. 元组类型")
print("=" * 50)

# 元组不可修改元素
t = (1,2,3,4,5)     # ( ) 生成元组
print(f"t = {t}")
print(f"t[0] = {t[0]}")
print(f"t[1:4] = {t[1:4]}")

# 元组和列表转换
ls_from_tuple = list(t)
print(f"元组转列表: {ls_from_tuple}")
ls_from_tuple[0] = 100
print(f"修改列表: {ls_from_tuple}")
t_from_list = tuple(ls_from_tuple)  # tuple
print(f"列表转元组: {t_from_list}")

print("\n + '=' * 50")
print("4. 字典类型")
print("=" * 50)

# 创建字典
d = {"name": "Go1", "joints": 12, "height": 0.4}
print(f"d = {d}")
print(f"d['name'] = {d['name']}")

# t添加/修改 键值对
d["weight"] = 12.5
print(f"添加weught后: {d}")
d["height"] = 4.5
print(f"修改height后: {d}")

# 字典操作
print(f"keys(): {list(d.keys())}")
print(f"values():{list(d.values())}")
print(f"items(): {list(d.items())}")

# get()方法
print(f"d.get('name') = {d.get('name')}")
print(f"d.get('price',0) = {d.get('price',0)}")

# 字典遍历
print("字典遍历:")
for key, value in d.items():
    print(f"{key}: {value}")

# 字典推导式
squares_dict = {x: x**2 for x in range(1,6)}
print(f"平方字典: {squares_dict}")

print("\n + '=' * 50")
print("5. 组合数据类型嵌套")
print("=" * 50)

# 列表中的字典

robots = [
    {"name": "Go1", "price": 16000},    # ← 添加逗号
    {"name": "B2", "price": 25000},     # ← 添加逗号
    {"name": "Aliengo", "price": 40000}
]

print("机器人列表:")
for robot in robots:
    print(f" {robot['name']}: {robot['price']}")

# 字典中的列表
robot_specs = {
    "Go1":{"joints":12,"sensors":["camera", "lidar", "imu"]},
    "B2":{"joints": 12, "sensors": ["camera", "lidar", "imu", "gps"]}
}
print(f"'Go1传感器: {robot_specs ['Go1'] ['sensors']}")

