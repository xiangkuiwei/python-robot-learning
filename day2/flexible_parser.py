# 写一个函数，能处理任意空格情况。
def parse_robot_state(data_string):
    pairs = data_string.split(",")
    results=[]
    for pair in pairs:
        pair = pair.strip( )
        parts = pair.split(":")
        joint_name = parts[0].strip()
        angle = float(parts[1].strip())
        results.append([joint_name,angle])
        print(f"关节{joint_name}的角度是{angle}rad")
    return results


print("测试 data1:")
data1 = "j1: 1.57, j2: 0.78, j3: -1.2"
parse_robot_state(data1)

print("\n测试 data2:")
data2 = "j1:   1.57 , j2:0.78 , j3:-1.2"
parse_robot_state(data2)


