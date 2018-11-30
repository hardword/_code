#!/bin/python
# http://hr.gs/bbfade

import string
alpha = string.ascii_lowercase

n = 3
L = []
for i in range(n):
	#print "Case: "+str(i)
	s = "-".join(alpha[i:n])
	#print "s: ", s
	#print "s[::-1]: ", s[::-1]
	#print "s[1:]: ", s[1:]
	L.append((s[::-1]+s[1:]).center(4*n-3, "-"))
	#print "L: ", L
	#print "\n"
print('\n'.join(L[:0:-1]+L))