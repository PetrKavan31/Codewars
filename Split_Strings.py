# Split Strings

# Complete the solution so that it splits the string into pairs of two characters.
# If the string contains an odd number of characters then it should replace the missing second character of the final pair with an underscore ('_').
#
# Examples:
#
# * 'abc' =>  ['ab', 'c_']
# * 'abcdef' => ['ab', 'cd', 'ef']


# ------------------------ MY SOLUTION: ----------------------------------------
def solution(s):
    if len(s) % 2 != 0:
        s += "_"
    # t = [s[i] for i in range(0, len(s), 2)]
    # r = [s[i] for i in range(1, len(s), 2)]
    # u = [t_e + r_e for t_e, r_e in zip(t, r)]
    return [s[i:i+2] for i in range(0, len(s), 2)]
    # return u


assert solution('abcdef') == ['ab', 'cd', 'ef']
assert solution('abc') == ['ab', 'c_']
assert solution('x') == ['x_']
assert solution("") == []

# ---------------------------- best practices, for example: ---------------------


def solution(s):
    result = []
    if len(s) % 2:
        s += '_'
    for i in range(0, len(s), 2):
        result.append(s[i:i+2])
    return result
