class Dog:

    # 초기화
    def __init__(self, pet_name, temp):
        self.name = pet_name
        self.temperature = temp


    def status(self):
        print("dog name is ", self.name)
        print("dog temperature is ", self.temperature)
        pass

    def set_temperature(self, temp):
        self.temperature = temp
        pass

    def bark(self):
        print("woof!")
        pass
    pass

lassie = Dog("Lassie", 37)

lassie.status()
# result
# dog name is  Lassie
# dog temperature is  37

lassie.set_temperature(15)
lassie.status()
# result
# dog name is  Lassie
# dog temperature is  15
