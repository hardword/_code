#!/bin/python
# http://hr.gs/ebfddb

#First Dumb Solution LOL I_No_Programmer
def possibleStacks(h):
    l=[]
    for i in xrange(len(h)):
        l.append(sum(h[len(h)-1-i:len(h)]))
    return l

def equalStacks(h1, h2, h3):
    if sum(h1) - sum(h2) -sum(h3) == 0:
        return sum(h1)
    else:
        inter = list(set(possibleStacks(h1)) & set(possibleStacks(h2)) & set(possibleStacks(h3)))
        if len(inter) == 0:
            return 0
        else:
            return max(inter)

# Slightly Better
def equalStacks(h1, h2, h3):
    d={0:h1, 1:h2, 2:h3}
    while True:
        t=[]
        for s in [h1, h2, h3]:
            if len(s) == 0:
                return 0
                break
            else:
                t.append(sum(s))
        if t[0] == t[1] and t[1] == t[2]:
            return t[0]
            break
        else:
            d[t.index(max(t))].pop(0)

# Just One Sum (slightly better)
def equalStacks(h1, h2, h3):
    d={0:h1, 1:h2, 2:h3}
    t=[]
    for s in [h1, h2, h3]:
            t.append(sum(s))
    while True:
        if t[0] == t[1] and t[1] == t[2]:
            return t[0]
            break
        else:
            stackIdx = t.index(max(t))
            d[stackIdx].pop(0)
            if len(d[stackIdx]) == 0:
                return 0
                break
            t[stackIdx] = sum(d[stackIdx])

# Finally Yeah~~~
def equalStacks(h1, h2, h3):
    s = [sum(h1), sum(h2), sum(h3)]
    d = {0:h1, 1:h2, 2:h3}
    while max(s) > min(s):
        h_maxs = d[s.index(max(s))]
        s[s.index(max(s))] -= h_maxs[0]
        h_maxs.pop(0)
    return s[0]  


s1 = '3 2 1 1 1'
s2 = '4 3 2'
s3 = '1 1 4 1'

s1 = '1'
s2 = '2'
s3 = '3'

h1 = map(int, s1.split())
h2 = map(int, s2.split())
h3 = map(int, s3.split())

print equalStacks(h1, h2, h3)