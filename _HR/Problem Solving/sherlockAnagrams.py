#!/bin/python
# http://hr.gs/ec3

s = 'kkkk'
n = len(s)

# all substrings
# cool one liner
l = [s[i:j+1] for i in xrange(n) for j in xrange(i,n)]

# for better understanding ('i' for starting character, 'j' for the length)
for i in xrange(n):
	for j in xrange(i,n):
		#print s[i:j+1]
		pass
		
from collections import defaultdict

s = 'kkkk'
n = len(s)

all = defaultdict(int)

# 'i' for length 'j' for starting character
for i in xrange(1,n):
	for j in xrange(n-i+1):
		substr = ''.join(sorted(s[j:j+i]))
		all[substr] += 1 

cnt = 0		
for i in all:
	cnt += (all[i]*(all[i]-1))/2

print cnt