class Animal:
    num_of_animal = 0
    def __init__(self):
        Animal.num_of_animal += 1


class Cat(Animal):
    def __init__(self):
        super().__init__()

    def meow(self):
        return print('야옹!')


cat1 = Cat()
cat1.meow()