import turtle

import numpy as np


class DrawFigure:
    def __init__(self):
        self.t = turtle.Turtle()
        self.t.shape('turtle')
        turtle.exitonclick()



    def circle(self):
        for x in np.linspace(start=0.1, stop=7, num=100):
            print(x)
            self.t.left(x)
            self.t.forward(x)


DrawFigure()
