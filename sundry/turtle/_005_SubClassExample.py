# 슈퍼클래스 Car

class Car:

    def __init__(self, name):
        self.name = name

    def getName(self):
        return self.name


class Truck(Car):
    def __init__(self, name):
        super().__init__(name)
        self.carrying_capacity()

    def carrying_capacity(self):
        print(f'{self.getName()}의 현재 적재량은 500kg 입니다.')


if __name__ == '__main__':
    truck = Truck("1톤 트럭")
