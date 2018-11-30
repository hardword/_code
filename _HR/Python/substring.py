#!/bin/python
# http://hr.gs/eeacfb, Minion Game

import collections

def get_all_substrings(str, length):
    if length == 1:
        l=list(str)
    else:
        l=[]
        for i in xrange(len(str)+1):
            if i+length <= len(str):
                substr=str[i:i+length]
                l.append(substr)
    return l


S = "BANANA"
D = {}
n=len(S)

ss=0
ks=0

for i in  xrange(1, n+1):
	D.update(collections.Counter(get_all_substrings(S, i)))


for i in D:
	if i[0] in ['A', 'E', 'I', 'O', 'U']:
		ks += D[i]
	else:
		ss += D[i]

if ks > ss:
	print "Kevin", ks
elif ks == ss:
	print "Draw"
else:
	print "Stuart", ss

	
