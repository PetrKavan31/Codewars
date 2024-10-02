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

def two_sum(numbers, target):
    for i in range(len(numbers)):
        a = target - numbers[i]
        for j in range(len(numbers)):
            if numbers[j] == a:
                break
    return (i,j)


assert two_sum([1, 2, 3], 4) == (0, 2) or (2, 0)
assert two_sum([3, 2, 4], 4) == (1, 2) or (2, 1)
