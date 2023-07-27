class Animal:
    num_of_animal = 0
    def __init__(self):
        Animal.num_of_animal += 1


class Dog(Animal):
    def __init__(self,sound):
        super().__init__()
        self.sound  = sound
    
    def bark(self):
        return print('멍멍 !')
    

class Cat(Animal):
    def __init__(self):
        super().__init__()

    def meow(self):
        return print('야옹 !')    


class Pet(Dog,Cat):
    def __init__(self, P_sound):
        super().__init__(P_sound)
        self.sound = P_sound
    
    def play(self):
        print('애완동물과 놀기')
    
    def make_sound(self):
        print(f'{self.sound}')
    

pet1 = Pet("그르르")
pet1.make_sound()
pet1.bark()
pet1.meow()
pet1.play()