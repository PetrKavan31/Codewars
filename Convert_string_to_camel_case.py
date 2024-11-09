# Complete the method/function so that it converts dash/underscore delimited words into camel casing.
# The first word within the output should be capitalized only if the original word was capitalized
# (known as Upper Camel Case, also often referred to as Pascal case).
# The next words should be always capitalized.
#
# Examples
# "the-stealth-warrior" gets converted to "theStealthWarrior"
#
# "The_Stealth_Warrior" gets converted to "TheStealthWarrior"
#
# "The_Stealth-Warrior" gets converted to "TheStealthWarrior"


def to_camel_case(c):
    parts = c.replace("-", "_").split('_')
    return parts[0] + "".join(i.capitalize() for i in parts[1:])


assert to_camel_case('the-Stealth-Warrior') == 'theStealthWarrior'
assert to_camel_case('The_Stealth_Warrior') == 'TheStealthWarrior'
assert to_camel_case('The_Stealth-Warrior') == 'TheStealthWarrior'
assert to_camel_case('') == ''
assert to_camel_case('A-B-C') == 'ABC'
assert to_camel_case('the_stealth-warrior') == 'theStealthWarrior'

# ------------------------- My first version -------------------------------

def to_camel_case(c):
    c = c.replace("-", "_")
    c = c.split('_')
    y = list(c[0])
    for i in c[1:]:
        x = i.capitalize()
        y.append(x)
    z = ''.join(y)
    return z
