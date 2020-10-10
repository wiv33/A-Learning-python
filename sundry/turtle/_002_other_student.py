import turtle

t = turtle.Turtle()
t.shape("turtle")


def remove(txt):
    t.pencolor(1, 1, 1)
    for x in range(7):
        t.write(txt)
    t.pencolor(0, 0, 0)


t.penup()
t.goto(100, 100)
t.write("거북이에게 양수를 주면 이리로 옵니다.")
t.goto(100, 0)
t.write("거북이에게 0을 주면 이리로 옵니다.")
t.goto(100, -100)
t.write("거북이에게 음수를 주면 이리로 옵니다.")

t.goto(0, 0)
t.pendown()

s = turtle.textinput("숫자 먹이", "거북이에게 줄 숫자를 입력하세요.")
n = int(s)

if n > 0:
    t.goto(100, 100)
    remove("거북이에게 양수를 주면 이리로 옵니다.")
    t.write('거북이에게 양수를 주셨군요.')
elif n == 0:
    t.goto(100, 0)
    remove("거북이에게 0을 주면 이리로 옵니다.")
    t.write('거북이에게 0을 주셨군요.')
else:
    t.goto(100, -100)
    remove("거북이에게 음수를 주면 이리로 옵니다.")
    t.write('거북이에게 음수를 주셨군요.')

turtle.exitonclick()