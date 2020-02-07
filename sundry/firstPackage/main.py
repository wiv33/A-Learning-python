class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_hello(self, to_name):
        print("안녕! " + to_name +" 나는 " + self.name)

    def introduce(self):
        print("내 이름은 " + self.name + " 그리고 나의 나이는 " + str(self.age))



myNamePrint = Person("print", 20)
# myNamePrint.say_hello(to_name="브라더")
myNamePrint.introduce()

