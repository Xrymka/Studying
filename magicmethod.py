class Square:
    square_list = []
    def __init__(self, n):
        self.name = n
        self.square_list.append(self.name)

    def __repr__(self):
        return("""{} on {} on {} on {}""".format(self.name, self.name, self.name, self.name))


square = Square(5)
square1 = Square(10)

print(square1)

def slag(a,b):
    print(a is b)

slag(5,5)
slag(10,5)
        
