import turtle

t = turtle.Turtle()
t.shape('turtle')

# 상단이동
t.penup()
t.left(90)
t.forward(100)
t.left(90)  ## 1번

# 상단 사각형

t.pendown()  ## 2번
t.forward(50)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(50)

# 하단 좌측 이동
t.penup()
t.left(30)
t.forward(100)

# 하단 좌측 삼각형
t.pendown()
t.left(30)
t.forward(150)
t.left(120)  ## 3번
t.forward(150)
t.left(120)  ## 3번
t.forward(150)

# 하단 우측 이동
t.penup()
t.right(120)
t.forward(200)
t.left(180)  # 4번

t.pendown()
t.circle(75)
turtle.exitonclick()