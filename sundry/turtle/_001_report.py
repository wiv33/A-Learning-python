import turtle

import numpy as np


class DrawFigure:
    def __init__(self):
        self.turtle = turtle
        self.t = self.turtle.Turtle()
        self.t.shape('turtle')

        self.move_pen(-300., -220.)
        self.t.circle(170)
        self.t.pencolor((0.2, 0.8, 0.55))
        self.circle()

        self.move_pen(-50., 300.)
        self.t.pencolor((1, 0, 0))
        self.polygon()

        self.move_pen(300., -220.)
        self.t.pencolor((0.7, 0.7, 0.55))
        self.rhombus()

        self.move_pen(0, 0)
        self.wait_close()

    def circle(self):
        for x in np.linspace(start=0.1, stop=7, num=100):
            self.t.right(x)
            self.t.forward(x)

    def polygon(self):
        for x in range(12):
            self.t.right(140)
            self.t.forward(70)
            self.t.left(170)
            self.t.forward(70)

    def rhombus(self):
        for x in range(8):
            self.t.left(45)
            self.t.forward(100)

        self.t.penup()
        self.t.forward(30)
        self.t.pendown()

        for x in range(12):
            self.t.right(30)
            self.t.forward(30)

    def move_pen(self, x: float, y: float):
        self.t.penup()
        self.t.setx(x)
        self.t.sety(y)
        self.t.pendown()

    def wait_close(self):
        self.turtle.exitonclick()


DrawFigure()
