#ConvertAngle  单关节 角度弧度 转换器 
pi = 3.14159
while True:
    print("关节角度转换")
    print("1.角度转化成弧度。")
    print("2.弧度转化为角度。")
    print("0.退出。")
    choice = input("请选择序号.")        # input()返回的是字符串类型，比如输入 0 得到的是字符串 "0"
    if choice == "0":                  # 故if语句中应该使用 if choice == "0"，而不是 if choice == 0.
        print("程序结束")
        break
    elif choice == "1":
        deg = float(input("请输入角度值:"))     # float()将其他数据类型转换为浮点数
        rad = deg * (pi/180)
        print("转化后的弧度为{:.2f}rad".format(rad))
    elif choice == "2":
        rad = float(input("请输入弧度值:"))
        deg = rad * (180/pi)
        print("转化后的角度为{:.2f}度".format(deg))
    else:
        print("无效选择，请重新输入。")
