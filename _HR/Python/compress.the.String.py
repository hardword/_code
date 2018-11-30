#!/bin/python
# http://hr.gs/baadff

s = raw_input()
l = [[1,int(s[0])]]

for i in xrange(len(s)-1):
	a=int(s[i])
	b=int(s[i+1])
	if a == b:
		if l[-1][1] == b:
			l[-1][0] += 1
	else:
		l.append([1,b])

for i in l:
	print (i[0], i[1]),

# itertools, groupby!!!

from itertools import groupby

print list(groupby(s))
	
li =[list(k) for k, k in groupby(s)] 

print li