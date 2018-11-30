#!/bin/python
# http://hr.gs/dfadfa

from collections import defaultdict

n, m = map(int, raw_input().split())
d = defaultdict(list)
l = []

for i in range(0,n):
    d[raw_input()].append(i+1) 

for j in range(0,m):
    l.append(raw_input())

for k in l: 
    if k in d:
        print " ".join( map(str,d[k]) )
    else:
        print -1
