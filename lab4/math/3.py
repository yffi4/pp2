import math
sides = int(input("Input number of sides: "))
if sides > 2:
    length = int(input("Input the length of a side: "))
    radius = length / (2 * math.tan(math.pi / sides))
    print(f"The area of the polygon is: {int(length * sides * radius / 2)}")
else:
    print("Such a polygon doesn't exist!")