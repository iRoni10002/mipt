from ex2_models import *

shape = Shape(1, 2)
triangle = Triangle(5, 5)
rectangle = Rectangle(5, 5)
print(shape, triangle.area(), rectangle.area(), '-------------------', sep='\n')

mother = Mother()
daughter = Daughter()
print(mother, daughter, '-------------------', sep='\n')

animal = Animal('Animal', 18)
zebra = Zebra('Mike', 9, 'smth about zebrs')
dolphin = Dolphin('Bob', 23, 'smth about dolphins')
print(
      animal.get_name(),
      animal.get_age(),
      animal,
      zebra.get_name(),
      zebra.get_age(),
      zebra,
      dolphin.get_name(),
      dolphin.get_age(),
      dolphin,
      '-------------------',
      sep='\n'
     )
