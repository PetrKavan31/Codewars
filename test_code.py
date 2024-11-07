def to_camel_case(c):
    c = c.replace("-", "_")
    c = c.split('_')
    # y = list()
    # y.append(c[0])
    y = list(c[0])
    for i in c[1:]:
        x = i.capitalize()
        y.append(x)
    z = ''.join(y)
    return z
