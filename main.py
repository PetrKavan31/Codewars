def to_camel_case(c):
    result = ''
    capitalize = False
    for char in c:
        if char in ('-', '_'):
            capitalize = True
        else:
            if capitalize:
                result += char.upper()
                capitalize = False
            else:
                result += char
    return result


assert to_camel_case('the-Stealth-Warrior') == 'theStealthWarrior'
assert to_camel_case('The_Stealth_Warrior') == 'TheStealthWarrior'
assert to_camel_case('The_Stealth-Warrior') == 'TheStealthWarrior'
assert to_camel_case('') == ''
assert to_camel_case('A-B-C') == 'ABC'
assert to_camel_case('the_stealth-warrior') == 'theStealthWarrior'

