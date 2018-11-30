#!/bin/python
# http://hr.gs/eddcca

from itertools import combinations_with_replacement

x = raw_input().split()

#string = sorted(set(list(x[0])))
string = sorted(list(x[0]))
k = int(x[1])
L = list(combinations_with_replacement(string,k))
	
for j in L:
	print ''.join(j)


