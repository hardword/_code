#!/bin/python
# http://hr.gs/fea

from collections import Counter

n = int(raw_input())
l = map(int, raw_input().split())
d = Counter(l)
o = int(raw_input())
s = 0

for i in xrange(o):
	m = map(int, raw_input().split())
	if d[m[0]] > 0:
		d[m[0]] -= 1
		s += m[1]

print s
