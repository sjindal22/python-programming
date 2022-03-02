from itertools import combinations

def threesum(l1: list) -> list:

    l = []
    neg = [x for x in l1 if x < 0]
    pos = [x for x in l1 if x > 0]
    zero = [x for x in l1 if x == 0]

    n = list(set(neg))
    p = list(set(pos))

    for x in p:
        if -1*x in n and len(zero) != 0:
            l.append([x, 0, -x])

    for x, y in combinations(neg, 2):
        t = -(x+y)
        if t in pos:
            l.append([x, y, t])

    for x, y in combinations(pos, 2):
        t = -(x+y)
        if t in neg:
            l.append([x, y, t])

    return l

print(threesum([-1, 0, 1, 2, -1, -4]))

'''
o/P: [[1, 0, -1], [-1, -1, 2]]
'''
