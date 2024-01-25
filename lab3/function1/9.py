import math


def volume(radius):
    vol = 4/3 * math.pi * math.pow(radius, 3)
    return vol


print("write your radius: ")
radius = int(input())
print(volume(radius))

