class Animal:
    num_of_animal = 0
    def __init__(self):
        Animal.num_of_animal += 1


class Dog(Animal):
    sound  = '멍멍'
    def __init__(self):
        super().__init__()
        
    def bark(self):
        return print('멍멍 !')
    
    def __str__(self):
        return f'애완동물은 {self.sound} 소리를 냅니다.'
    

class Cat(Animal):
    sound  = '야옹'
    def __init__(self):
        super().__init__()

    def meow(self):
        return print('야옹 !')
    
    def __str__(self):
        return f'애완동물은 {self.sound} 소리를 냅니다.'    

#Dog 우선상속
class Pet(Dog,Cat):
    def __init__(self):
        super().__init__()

    @classmethod
    def __str__(cls):
        return f'애완동물은 {cls.sound} 소리를 냅니다.'


p1 = Pet()
print(p1)