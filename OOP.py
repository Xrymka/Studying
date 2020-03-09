class Apple:
    def __init__(self, c, s, f, v):
        self.color = c
        self.size = s
        self.flavour = f
        self.view = v
        print("Создано!")

import math    
class Circle:
    def __init__(self, r):
        self.radius = r
        print("Создано!")

    def area(self):
        return self.radius * self.radius * math.pi

circle = Circle(3)
print(circle.area())

class Triangle:
    def __init__(self, b, h):
        self.base = b
        self.height = h

    def area(self):
        return 1/2 * self.base * self.height

triangle = Triangle(2,4)
print(triangle.area())


class Hexagon:
    def __init__(self, s):
        self.side = s

    def calculate_perimeter(self):
        return self.side * 6

hexagon = Hexagon(5)
print(hexagon.calculate_perimeter())
