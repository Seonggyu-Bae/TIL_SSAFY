class Shape:
   def __init__(self,w,h):
      self.width = w
      self.height =h

   def calculate_area(self):
      return self.width * self.height
    
   def calculate_perimeter(self):
      return 2*(self.width + self.height)

   def print_info(self):
      print(f'Width: {self.width}')
      print(f'Height: {self.height}')
      print(f'Area: {self.calculate_area()}')
      print(f'Perimeter: {self.calculate_perimeter()}')

shape1 = Shape(5, 3)
shape1.print_info()