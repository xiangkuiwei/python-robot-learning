# 科赫雪花 - 递归分形
import turtle

def setup_turtle():
    turtle.setup(800,600)
    turtle.penup()
    turtle.goto(-300,100)
    turtle.pendown()
    turtle.pensize(2)
    turtle.speed(10)
    turtle.color("blue")

def koch(size, n):
    # size 当前要画的线段长度 n 当前的递归深度
    if n == 0:
        turtle.fd(size)
        return   
    # 把一条直线分为四段，前进 -> 左转60 -> 右转120 ->前进 -> 左转60 -> 前进
    for angle in [0,60,-120,60]:
        turtle.left(angle)
        koch(size/3,n-1)     # 调用递归函数，花更小的线段。

def snowflake(size,n):
    for i in range(3):
        koch(size,n)
        turtle.right(120) # 等边三角形，三条边，画完一条转120度，进入下一条边。

def draw_multiple():
    positions = [(-300,200),(-300,-100),(100,50)]
    colors = ["blue", "green", "red"]
    sizes = [300,300,150]
    depths = [1,2,3]
    names = ["一阶雪花", "二阶雪花", "三阶雪花",]
    for i in range(3):
        turtle.penup()
        turtle.goto(positions[i])
        turtle.pendown()
        turtle.color(colors[i])
        turtle.pensize(2)

        print(f"绘制{colors[i]}{names[i]},阶数={depths[i]}")
        snowflake(sizes[i],depths[i])

        turtle.penup()
        turtle.goto(positions[i][0],positions[i][1]-50)
        turtle.write(f"{names[i]}",font=("Arial",16,"normal"))

def done():
    turtle.hideturtle()
    turtle.done()

def main():
    setup_turtle()
    draw_multiple()
    done()
    
if __name__ == "__main__":
    main()





