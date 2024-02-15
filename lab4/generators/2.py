def gen(num):

    for i in range(num + 1):
        if i % 2 == 0:
            yield i


n = gen(int(input()))
print(','.join(map(str, n)))