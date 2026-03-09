#原始数据
data = "j1:1.57,j2:0.78,j3:-1.2"
pairs = data.split(",")   # 错误用法: data.split(,)
for pair in pairs:
    parts = pair.split(":")
    joint_name = parts[0]
    angle = float(parts[1])
    print(f"关节{joint_name}的角度是{angle}rad")   
    
    #这里的print得放在for循环里面，注意缩进。

# 把解析结果存成列表，每个元素是 [关节名, 角度] 的形式。
data = "j1:1.57,j2:0.78,j3:-1.2"
joints = []
pairs = data.split(",")   
for pair in pairs:
    parts = pair.split(":")
    joint_name = parts[0]
    angle = float(parts[1])
    print(f"关节{joint_name}的角度是{angle}rad") 
    joints.append([joint_name,angle])  # append() 用于在列表末尾添加新元素。
print(joints)
    
#在解析的基础上, 计算并输出: 关节总数, 最大角度值, 最小角度值, 平均角度.
data = "j1:1.57,j2:0.78,j3:-1.2"
joints = []
pairs = data.split(",")   
for pair in pairs:
    parts = pair.split(":")
    joint_name = parts[0]
    angle = float(parts[1])
    print(f"关节{joint_name}的角度是{angle}rad") 
    joints.append([joint_name,angle])
angles = [item[1] for item in joints]
print(f"关节总数: {len(joints)}")
print(f"最大角度值: {max(angles):.2f}")
print(f"最小角度值: {min(angles):.2f}")
print(f"平均角度值: {sum(angles)/len(angles):.2f}")