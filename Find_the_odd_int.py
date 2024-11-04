# Find the odd int

# Given an array of integers, find the one that appears an odd number of times.
#
# There will always be only one integer that appears an odd number of times.
#
# Examples
# [7] should return 7, because it occurs 1 time (which is odd).
# [0] should return 0, because it occurs 1 time (which is odd).
# [1,1,2] should return 2, because it occurs 1 time (which is odd).
# [0,1,0,1,0] should return 0, because it occurs 3 times (which is odd).
# [1,2,2,3,3,3,4,3,3,3,2,2,1] should return 4, because it appears 1 time (which is odd).

# ---------------------------- My first solution -----------------------------
def find_it(a):
    for i in range(len(a)):
        count = 0
        for j in range(len(a)):
            if a[i] == a[j]:
                count += 1
        if count % 2 != 0:
            return a[i]

# ----------------------------- My best solution ---------------------------

from collections import Counter


def find_it(seq):
    return next(d for d, i in Counter(seq).items() if i % 2 != 0)


assert find_it([7]) == 7
assert find_it([0]) == 0
assert find_it([1, 1, 2]) == 2
assert find_it([0, 1, 0, 1, 0]) == 0
assert find_it([1, 2, 2, 3, 3, 3, 4, 3, 3, 3, 2, 2, 1]) == 4

# ---------------------------- best practices. example from CW -------------------------------


def find_it(seq):
    for i in seq:
        if seq.count(i) % 2 != 0:
            return i

# ------------------------------ clever, example from CW --------------------------------------


def find_it(seq):
    result = 0
    for x in seq:
        result ^= x
    return result


# ---------------------------- my test ---------------------------------------------------


def count_occurrence(a):
    d = {}
    for i in a:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1

    #     x = a.count(i)
    #     d.update({i: x})
    #
    return d


# b = [12, 8, 8, 42, 42, 42, 12]
# print(count_occurrence(b))


def key_with_odd_value():
    for key, val in count_occurrence(b).items():
        if val % 2 != 0:
            return key


b = [12, 8, 8, 42, 42, 42, 12]
print(key_with_odd_value())
