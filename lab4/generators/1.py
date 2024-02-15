
def power(x):
    for i in range(x):
        yield i**2

print(list(power(10)))

def power2(c):
    i = 0
    while i**2 < c:
        yield i**2
        i += 1

print(list(power2(10)))