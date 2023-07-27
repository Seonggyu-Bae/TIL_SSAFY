class Shape:
   def __init__(self,w,h):
      self.width = w
      self.height =h

   def __str__(self):
      return f'Shape: width={self.width}, height={self.height}'  
   
shape1 = Shape(5, 3)
print(shape1)