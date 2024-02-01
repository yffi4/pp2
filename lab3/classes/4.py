class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        print(f"x coordinate = {self.x}, y.coordinate = {self.y}")

    def move(self, update_x, update_y):
        self.x = update_x
        self.y = update_y

    def dist(self):
        print(self.x - self.y)


x = Point(2, 4)
x.show()
x.move(5, 6)
x.dist()
