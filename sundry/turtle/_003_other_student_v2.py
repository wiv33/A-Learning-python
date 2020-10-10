import turtle

base = [
    (100, 100, '거북이에게 양수를 주면 이리로 옵니다.'),
    (100, 0, '거북이에게 0을 주면 이리로 옵니다.'),
    (100, -100, '거북이에게 음수를 주면 이리로 옵니다.'),
]

result = [
    '거북이에게 양수를 주셨군요.',
    '거북이에게 0을 주셨군요.',
    '거북이에게 음수를 주셨군요.'
]

t = turtle.Turtle()
t.shape("turtle")


def write_base():
    for x, y, txt in base:
        t.penup()
        t.goto(x, y)
        t.pendown()
        t.write(txt)

    t.penup()
    t.goto(0, 0)


write_base()


def choice(cnt=1):
    x, y, txt = base[cnt]
    t.pendown()
    t.goto(x, y)
    t.penup()
    t.pencolor(1, 1, 1)
    for x in range(33):
        t.write(txt)
    t.pencolor(0., 0., 0.)
    t.write(result[cnt])


s = turtle.textinput("숫자 먹이", "거북이에게 줄 숫자를 입력하세요.")
n = int(s)

if n > 0:
    choice(0)
elif n == 0:
    choice(1)
else:
    choice(2)


turtle.exitonclick()
