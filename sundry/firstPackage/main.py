class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_hello(self, to_name):
        print("안녕! " + to_name +" 나는 " + self.name)

    def introduce(self):
        print("내 이름은 " + self.name + " 그리고 나의 나이는 " + str(self.age))



# myNamePrint = Person("print", 20)
# myNamePrint.say_hello(to_name="브라더")
# myNamePrint.introduce()

class Police(Person):
    def arrest(self, to_arrest):
        print("넌 체포됐다 %s" % to_arrest)

class Programmer(Person):
    def program(self, to_program):
        print("i'm make %s" % to_program)


jenny = Police("제임", 17)

jenny.introduce()
jenny.arrest("모랄")