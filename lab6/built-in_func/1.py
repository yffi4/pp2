import functools
lst = map(int, list(input().split()))
print(functools.reduce(lambda x, y: x * y, lst))
