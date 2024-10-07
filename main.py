# Two sum

# Write a function that takes an array of numbers (integers for the tests) and a target number.
# It should find two different items in the array that, when added together, give the target value.
# The indices of these items should then be returned in a tuple / list (depending on your language) like so: (index1, index2).
#
# For the purposes of this kata, some tests may have multiple answers; any valid solutions will be accepted.
#
# The input will always be valid (numbers will be an array of length 2 or greater, and all of the items will be numbers;
# target will always be the sum of two different items from that array).
#
# Based on: https://leetcode.com/problems/two-sum/

import itertools


def two_sum(numbers, target):
    return next((i, j) for i, j in itertools.combinations(range(len(numbers)), 2) if numbers[i] + numbers[j] == target)


print(two_sum([1, 2, 3], 4))
assert two_sum([1, 2, 3], 4) in ((0, 2), (2, 0))
print(two_sum([3, 2, 4], 6))
assert two_sum([3, 2, 4], 6) in ((1, 2), (2, 1))
print(two_sum([2, 1, 3, 8], 4))
assert two_sum([2, 1, 3, 8], 4) in ((1, 2), (2, 1))



