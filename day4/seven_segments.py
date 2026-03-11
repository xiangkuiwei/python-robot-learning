# 七段数码管绘制
import turtle
import time
def setup_turtle():
    turtle.setup(800,350,200,200)
    turtle.penup()
    turtle.goto(-350,0)
    turtle.pensize(5)
    turtle.speed(5)
    turtle.setheading(0)

def draw_gap():
    # 绘制数码管间隔
    turtle.penup()
    turtle.fd(5)

def draw_line(draw):
    # 绘制单段数码管
    draw_gap()
    turtle.pendown() if draw else turtle.penup()
    turtle.fd(40)
    draw_gap()
    turtle.right(90)

def draw_digit(digit):
    # 根据数字绘制七段数码管
    draw_line(True) if digit in [2,3,4,5,6,8,9] else draw_line(False)
    draw_line(True) if digit in [0,1,3,4,5,6,7,8,9] else draw_line(False)
    draw_line(True) if digit in [0,2,3,5,6,8,9] else draw_line(False)
    draw_line(True) if digit in [0,2,6,8] else draw_line(False)
    turtle.left(90)  # 修正方向
    draw_line(True) if digit in [0,4,5,6,8,9] else draw_line(False)
    draw_line(True) if digit in [0,2,3,5,6,7,8,9] else draw_line(False)
    draw_line(True) if digit in [0,1,2,3,4,7,8,9] else draw_line(False)
    turtle.left(180)
    turtle.penup()
    turtle.fd(20)

def draw_number(num):
    # 绘制一个数字
    for digit in str(num):
        draw_digit(int(digit))

def draw_date(date_str):
    # 绘制日期 支持分隔符
    turtle.pencolor("red")
    for char in date_str:
        if char == '-':
            turtle.write('年', font = ("Arial", 18, "normal"))
            turtle.pencolor("green")
            turtle.fd(40)
        elif char == '=':
            turtle.write('月', font = ("Arial", 18, "normal"))
            turtle.pencolor("blue")
            turtle.fd(40)
        elif char == '+':
            turtle.write('日', font = ("Arial", 18, "normal"))
        elif char.isdigit():
            draw_digit(int(char))

def show_current_time():
    # 显示当前时间, time.strftime(格式, 时间) - 将时间格式化为指定字符串。
    current = time.strftime("%Y-%m=%d+",time.localtime())
    print(f"当前时间格式: {current}")
    draw_date(current)

def done():
    turtle.hideturtle()       # 隐藏小海龟图标
    turtle.done()             # 保持绘图窗口打开, 如果不加这一行，窗口会一闪而过。

def main():
    setup_turtle()
    print("绘制数字 1234567890")
    draw_number(1234567890)

    turtle.clear()
    turtle.penup()
    turtle.goto(-350,0) # 让turtle回到左端重新开始绘制

    print("绘制当前时间")
    show_current_time()
    done()
if __name__ == "__main__":
    main()


