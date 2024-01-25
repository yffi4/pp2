from itertools import permutations


def perm(b):
    per = permutations(b)
    for i in per:
        print(' '.join(i))


perm('bca')

