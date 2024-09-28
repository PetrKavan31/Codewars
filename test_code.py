def solution(s):
    if len(s) % 2 != 0:
        s += "_"
    # t = [s[i] for i in range(0, len(s), 2)]
    # r = [s[i] for i in range(1, len(s), 2)]
    # u = [t_e + r_e for t_e, r_e in zip(t, r)]
    return [s[i:i+2] for i in range(0, len(s), 2)]
    # return u
