# 支持多种分隔符
def parse_robot_state_flexible(data_string, pair_sep=",", kv_sep=":"):
    pairs = data_string.split(pair_sep)    # 按指定的 pair_sep 分割
    results = []
    for pair in pairs:
        pair = pair.strip()
        if not pair:                       # 跳过空字符串
            continue
        parts = pair.split(kv_sep)         # 按指定的 kv_sep 分割
        if len(parts) != 2:
            print(f"警告:'{pair}'格式不正确,已跳过")
            continue
        joint_name = parts[0].strip()
        try:
            angle = float(parts[1].strip())
            results.append([joint_name,angle])
            print(f"关节{joint_name}角度是{angle}rad")
        except ValueError:
            print(f"警告:'{parts[1]}'不是有效数字，已跳过")
    return results

print("测试逗号分隔:")
data1 = "j1:1.57,j2:0.78,j3:-1.2"
result1 = parse_robot_state_flexible(data1)
print(f"结果: {result1}") 

print("\n测试分号分隔:")
data2 = "j1:1.57;j2:0.78;j3:-1.2"
result2 = parse_robot_state_flexible(data2, pair_sep=";")
print(f"结果: {result2}") 


