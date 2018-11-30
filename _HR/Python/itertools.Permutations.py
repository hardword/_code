#!/bin/python
# http://hr.gs/ffaeaa

from itertools import permutations

x = raw_input().split()

string = x[0]
k = int(x[1])

l=sorted(list(permutations(string,k)))

for i in l:
	print ''.join(i)


