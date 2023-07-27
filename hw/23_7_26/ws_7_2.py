class Shape:
   def __init__(self,w,h):
      self.width = w
      self.height = h

   def calculate_area(self):
      return self.width * self.height

shape1 = Shape(5, 3)
area1 = shape1.calculate_area()
print(area1)