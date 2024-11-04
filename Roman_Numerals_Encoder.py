def solution(c):

    a = ((1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
         (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
         (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I'))
    aa = []
    for i in a:
        if c // i[0] == 1:
            c = c - i[0]
            aa.append((i[1]))
        if c // i[0] == 2:
            c = c - (i[0]*2)
            aa.append(2*(i[1]))
        if c // i[0] == 3:
            c = c - (i[0]*3)
            aa.append(3*(i[1]))
    return "".join(aa)


assert solution(1889) == 'MDCCCLXXXIX'
assert solution(1) == 'I'
assert solution(984) == 'CMLXXXIV'
assert solution(21) == 'XXI'
