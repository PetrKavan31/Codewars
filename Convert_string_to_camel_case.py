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


a = 'the-Stealth-Warrior'
b = 'The_Stealth_Warrior'
c = 'The_Stealth-Warrior'
d = ''
e = 'A-B-C'
f = 'the_stealth-warrior'


x = f.split('_')
y = list()
y.append(x[0])
for i in x[1:]:
    x = i.capitalize()
    y.append(x)
w = ''.join(y)
# print(w)

n = w.split('-')
z = list()
z.append(n[0])
for i in n[1:]:
    n = i.capitalize()
    z.append(n)
m = ''.join(z)
print(m)


# assert to_camel_case('the-Stealth-Warrior') == 'theStealthWarrior'
# assert to_camel_case('The_Stealth_Warrior') == 'TheStealthWarrior'
# assert to_camel_case('The_Stealth-Warrior') == 'TheStealthWarrior'
# assert to_camel_case('') == ''
# assert to_camel_case('A-B-C') == 'ABC'
# assert to_camel_case('the_stealth-warrior') == 'theStealthWarrior'
