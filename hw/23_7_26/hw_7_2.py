class StringRepeater:
   def __init__(self):
      pass
   def repeat_string(self,count,my_str):
      for _ in range(count):
         print(my_str)
      
repeater1 = StringRepeater()
repeater1.repeat_string(3, "Hello")