from collections import Counter


def key_with_odd_value():
    return next(d for d, i in Counter(b).items() if i % 2 != 0)


b = [12, 8, 8, 42, 12]
print(key_with_odd_value())
