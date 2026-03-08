# JointAngleConvert
while True:
    n = int(input("请输入关节数量:"))    #关节数量为整数应该使用int().
    print("请选择转化方向:")
    print("1.角度转化为弧度。")
    print("2.弧度转化为角度。")
    choice = input("请选择序号:")
    pi=3.14159
    values = []   # values 创建空列表准备存储
    print()
    for i in range(n):
        if choice == "1":
            val = float(input(f"第{i+1}个关节角度值:"))
            values.append(val)    # append()是列表的一个方法，用于在列表的末尾添加一个新元素。  
        elif choice == "2":
            val = float(input(f"第{i+1}个关节弧度值:"))
            values.append(val)
    print("转化结果:")
    for i, val in enumerate(values,1):     # 从1开始索引 迭代values中每个值。
        if choice == "1":
            result = val * (pi/180)
            print(f"关节{i}: {val:.2f}度 转化为 {result:.4f}rad")
        elif choice == "2":
            result = val * (180/pi)
            print(f"关节{i}: {val:.4f}rad 转化为 {result:.2f}度")
    if input("\n 继续? (y/n):").lower() != 'y':  ## .lower(): 将字符串中的所有字母转换为小写。
        break
        
        
