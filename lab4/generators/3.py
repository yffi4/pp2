def iterate(num):
    for i in range(num + 1):
         if i & 3 == 0 and i % 4 == 0:
             yield i


n = iterate(100)
for i in n:
    print(i)