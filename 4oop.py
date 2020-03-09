class Rectangle:
    def __init__(self, a, b):
        self.sidea = a
        self.sideb = b

    def calculate_perimeter(self):
        return (self.sidea + self.sideb) * 2

class Square():
    def __init__(self, a):
        self.sidea = a

    def calculate_perimeter(self):
        return self.sidea * 4

    def change_size(self, s):
        self.sidea += s

rectangle = Rectangle(3,4)
square = Square(5)
print(rectangle.calculate_perimeter())
print(square.calculate_perimeter())
square.change_size(10)
print(square.sidea)

class Horse():
    def __init__(self, n, b, o):
        self.name = n
        self.breed = b
        self.owner = o

class Rider():
    def __init__(self, n):
        self.name = n

Den = Rider("Даниил Балашов")
Hope = Horse("Hope", "Mustang", Den)
print(Hope.owner.name)

class Shape():
    def what_am_i(self):
        print("Я - фигура")

class Rectangle(Shape):
    def __init__(self, width, length):
        self.width = width
        self.length = length

    def calculate_perimeter(self):
        return self.width * 2 + self.length * 2


class Square(Shape):
    def __init__(self, s1):
        self.s1 = s1

    def calculate_perimeter(self):
        return self.s1 * 4

a_rectangle = Rectangle(20, 50)
a_square = Square(29)

a_rectangle.what_am_i()
a_square.what_am_i()


    
