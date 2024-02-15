def square(a, b):
    for i in range(a, b+1):
        yield i**2

n = square(1, 54)
for i in n:
    print(i)