import turtle as t
t.title("自动轨迹绘制")
t.setup(800,600,0,0)
t.pencolor("red")
t.pensize(5)

# 数据读取
datals = []
f = open("data.txt")
for line in f:
    line = line.replace("\n","")       # 去除每行末尾的换行符
    # 用逗号分割字符串，对每个元素使用eval()转换为数字，再转换为列表，添加到datals中
    datals.append(list(map(eval,line.split(","))))
f.close

# line.split(",")  # 假设 line = "300,0,144,1,0,0"
# 结果: ["300", "0", "144", "1", "0", "0"]  (字符串列表)

# map(eval, ["300", "0", "144", "1", "0", "0"])
# 将eval函数应用到每个字符串上
# 结果: 一个map对象，包含 [300, 0, 144, 1, 0, 0]  (数字列表)

# list(map(eval, line.split(",")))
# 将map对象转换为列表
# 最终结果: [300, 0, 144, 1, 0, 0]


# 自动绘制
for i in range(len(datals)):
    t.pencolor(datals[i][3],datals[i][4],datals[i][5])
    t.fd(datals[i][0])
    if datals[i][1]:
        t.right(datals[i][2])
    else:
        t.left(datals[i][2])

# 隐藏海龟并完成
t.hideturtle()
t.done()