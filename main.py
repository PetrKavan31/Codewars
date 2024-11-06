a = 'the-Stealth-Warrior'
b = 'The_Stealth_Warrior'
c = 'The_Stealth-Warrior'
d = ''
e = 'A-B-C'
f = 'the_stealth-warrior'

x = a.split('_')
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

