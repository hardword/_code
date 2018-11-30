#!/bin/python
# http://hr.gs/f50

from itertools import combinations

x = raw_input().split()

#string = sorted(set(list(x[0])))
string = sorted(list(x[0]))
k = int(x[1])
L = []

for i in xrange(1,k+1):
	L += list(combinations(string,i))
	
for j in L:
	print ''.join(j)


