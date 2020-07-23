from dataclasses import dataclass


@dataclass()
class Rectangle:
    width: int
    height: int

    def area(self):
        return self.width * self.height


rectangle = Rectangle(3, 4)
print(rectangle.area())
# 12

