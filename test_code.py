def to_camel_case(c):
    c = c.replace("-", "_")
    c = c.split('_')
    y = list(c[0])
    for i in c[1:]:
        x = i.capitalize()
        y.append(x)
    z = ''.join(y)
    return z


assert to_camel_case('the-Stealth-Warrior') == 'theStealthWarrior'
assert to_camel_case('The_Stealth_Warrior') == 'TheStealthWarrior'
assert to_camel_case('The_Stealth-Warrior') == 'TheStealthWarrior'
assert to_camel_case('') == ''
assert to_camel_case('A-B-C') == 'ABC'
assert to_camel_case('the_stealth-warrior') == 'theStealthWarrior'
