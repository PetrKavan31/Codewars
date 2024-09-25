s = 'abcd'
t = []
r = []
u = []
#if len(s) % 2 != 0:
    #s.append('_')
for i in range(0, len(s), 2):
#for i in range(len(s)):
    t.append(s[i])

    #t = t + s[i]
print(t)
for i in range(1, len(s), 2):
    r.append(s[i])

print(r)
for i in range(len(t)):
    u.append(t[i] + r[i])
print(u)
