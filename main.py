from collections import Counter


def count_occurrence(a):
    cnt = Counter()
    for i in a:
        cnt[i] += 1
    return cnt


def key_with_odd_value():
    return next(d for (d, i) in count_occurrence(b).items() if i % 2 != 0)


b = [12, 8, 8, 42, 12]
print(key_with_odd_value())
