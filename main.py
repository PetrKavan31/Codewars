from collections import Counter


def count_occurrence(a):
    return Counter(a)


def key_with_odd_value():
    return next(d for d, i in count_occurrence(b).items() if i % 2 != 0)


b = [12, 8, 8, 42, 12]
print(key_with_odd_value())
