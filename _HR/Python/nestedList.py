#!/bin/python
# http://hr.gs/eq5

from collections import defaultdict
d = defaultdict(list)
s = []
for _ in range(int(raw_input())):
    name = raw_input()
    score = float(raw_input())
    d[score].append(name)
    s.append(score)

s = sorted(list(set(s)))
r = sorted(d[s[1]])

for n in r:
    print n