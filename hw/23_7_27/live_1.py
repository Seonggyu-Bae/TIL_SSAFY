class Person:
    gene  = 'XYZ'

    def __init__(self, name):
        self.name = name
        
    def greeting(self):
        return f'반갑습니다, {self.name}'


class Mom(Person):
    gene = 'XX'
    
    def __init__(self, name):
        super().__init__(name)

    def swim(self):
        return '엄마가 수영'


class Dad(Person):
    gene = 'XY'

    def __init__(self, name):
        super().__init__(name)

    def walk(self):
        return '아빠가 걷기'

class FirstChild(Dad, Mom):
    mom_gene = Mom.gene

    def __init__(self, name):
        super().__init__(name)

    def swim(self):
        return '첫째가 수영'
    
    def cry(self):
        return '첫째가 응애'
    
    
baby1 = FirstChild('아가')

print(baby1.cry())
print(baby1.swim())
print(baby1.walk())
print(baby1.gene) #Dad가 상속 순서가 앞이기 때문에 XY를 받음
print(baby1.mom_gene)

print(FirstChild.mro())