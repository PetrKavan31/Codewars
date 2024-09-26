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

    for i in range(0, len(s), 2):
        t.append(s[i])

    if len(s) % 2 != 0:
        for i in range(1, len(s), 2):
            r.append(s[i])
        r.append("_")
    else:
        for i in range(1, len(s), 2):
            r.append(s[i])

    for i in range(len(t)):
        u.append(t[i] + r[i])
    return u


print(solution('abcd'))
print(solution('abc'))
print(solution('a'))
print(solution(""))



