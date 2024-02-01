class Shape():
    def __init__(self):
        self.area = 0
'''
    def printarea(self):
        print(self.area)
'''

class Square(Shape):
    def __init__(self, length):
        self.length = length
    def area(self):
        print(self.length**2)

x = Square(10)
x.area()
 # x.printarea()
