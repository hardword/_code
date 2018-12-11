#!/bin/python

s = raw_input()
l,u,o,e=[],[],[],[]

for c in s:
    if c.islower():
        l.append(c)
    elif c.isupper():
        u.append(c)
    elif int(c)%2 == 1:
        o.append(c)
    else:
        e.append(c)
print ''.join(sorted(l))+''.join(sorted(u))+''.join(sorted(o))+''.join(sorted(e))

#leet1
order = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1357902468'
print ''.join(sorted(s, key=order.index))

#leet2
print ''.join(sorted(s, key=lambda c: (c.isdigit() - c.islower(), c in '02468', c)))

#leet3
f=[]
for x in s:
    f.append((x.isdigit(), x.isdigit() and int(x)%2==0, x.isupper(), x.islower(), x))
print ''.join(x[4] for x in sorted(f))


    