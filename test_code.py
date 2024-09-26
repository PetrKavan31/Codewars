s = list('abcd')
print(s)
t = []
r = []
u = []
#w = []
#if len(s) % 2 != 0:
    #for i in range(len(s)):
        #w.append(s[i])
    #w.append("_")
    #print(w)
for i in range(0, len(s), 2):
#for i in range(len(s)):
    t.append(s[i])

    #t = t + s[i]
print(t)
if len(s) % 2 != 0:
    for i in range(1, len(s), 2):
        r.append(s[i])
    r.append("_")
else:
    for i in range(1, len(s), 2):
        r.append(s[i])

print(r)
for i in range(len(t)):
    u.append(t[i] + r[i])
print(u)
