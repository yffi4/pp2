def decreasing(num):
    for i in range(num, -1, -1):
        yield i

n = decreasing(10)
for i in n:
    print(i)