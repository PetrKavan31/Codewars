# Split Strings

# Complete the solution so that it splits the string into pairs of two characters.
# If the string contains an odd number of characters then it should replace the missing second character of the final pair with an underscore ('_').
#
# Examples:
#
# * 'abc' =>  ['ab', 'c_']
# * 'abcdef' => ['ab', 'cd', 'ef']


def solution(s):

    t = []
    r = []
    u = []

    #for i in range(0, len(s), 2):
        #t.append(s[i])

    t = [s[i] for i in range(0, len(s), 2)]

    if len(s) % 2 != 0:
        for i in range(1, len(s), 2):
            r.append(s[i])
        r.append("_")

    #    r = [s[i] for i in range(1, len(s), 2) and r.append("_") if len(s) % 2 != 0]

    else:
        for i in range(1, len(s), 2):
            r.append(s[i])

    for i, t-element in enumerate(t):
        u.append(t-element + r[i])

   # u = [u.append(t[i] + r[i]) for i in range(len(t))]

    return u


assert solution('abcdef') == ['ab', 'cd', 'ef']
assert solution('abc') == ['ab', 'c_']
assert solution('x') == ['x_']
assert solution("") == []



