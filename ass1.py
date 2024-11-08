import turtle as t

# 设置画布
t.setup(width=600, height=600)
t.speed(3)

# 画猫的头
t.penup()
t.goto(0, -50)
t.pendown()
t.color("gray")
t.begin_fill()
t.circle(100)  # 猫头的大小
t.end_fill()

# 左耳
t.penup()
t.goto(-70, 50)
t.pendown()
t.begin_fill()
t.goto(-110, 160)
t.goto(-30, 100)
t.goto(-70, 50)
t.end_fill()

# 右耳
t.penup()
t.goto(70, 50)
t.pendown()
t.begin_fill()
t.goto(110, 160)
t.goto(30, 100)
t.goto(70, 50)
t.end_fill()

# 左眼
t.penup()
t.goto(-40, 20)
t.pendown()
t.color("white")
t.begin_fill()
t.circle(15)
t.end_fill()

# 左眼瞳孔
t.penup()
t.goto(-40, 30)
t.pendown()
t.color("black")
t.begin_fill()
t.circle(5)
t.end_fill()

# 右眼
t.penup()
t.goto(40, 20)
t.pendown()
t.color("white")
t.begin_fill()
t.circle(15)
t.end_fill()

# 右眼瞳孔
t.penup()
t.goto(40, 30)
t.pendown()
t.color("black")
t.begin_fill()
t.circle(5)
t.end_fill()

# 鼻子
t.penup()
t.goto(0, 0)
t.pendown()
t.color("pink")
t.begin_fill()
t.goto(-10, -10)
t.goto(10, -10)
t.goto(0, 0)
t.end_fill()

# 嘴巴
t.penup()
t.goto(-10, -20)
t.pendown()
t.setheading(-60)
t.circle(10, 120)  # 左嘴
t.penup()
t.goto(10, -20)
t.pendown()
t.setheading(-120)
t.circle(-10, 120)  # 右嘴

# 胡须
whiskers = [(-30, -5, -80), (-30, -15, -60), (-30, -25, -40),
            (30, -5, 80), (30, -15, 60), (30, -25, 40)]
for x, y, angle in whiskers:
    t.penup()
    t.goto(x, y)
    t.setheading(angle)
    t.pendown()
    t.forward(40)

# 完成
t.hideturtle()
t.done()
