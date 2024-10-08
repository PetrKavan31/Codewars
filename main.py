from collections import Counter


def find_it(seq):
    return next(d for d, i in Counter(seq).items() if i % 2 != 0)


seq = [0, 1, 1, 1, 0]
print(find_it(seq))
