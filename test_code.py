
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
