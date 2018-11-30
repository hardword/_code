#!/bin/python
# http://hr.gs/elz

import itertools

l=int(raw_input())
c=range(1,l+1)
s=raw_input().split()
n=int(raw_input())

i=[i+1 for i, e in enumerate(s) if e == 'a']

cn=0
dn=0

for t in itertools.combinations(c,n):
	dn += 1
	if bool(set(t) & set(i)):
		cn += 1

print (cn*1.0)/dn