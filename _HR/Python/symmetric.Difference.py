#!/bin/python
# http://hr.gs/aeedae

# Enter your code here. Read input from STDIN. Print output to STDOUT
m = int(raw_input())
M = set(map(int, raw_input().split()))
n = int(raw_input())
N = set(map(int, raw_input().split()))
#L = sorted(list(M.union(N)-M.intersection(N)))
L = sorted(list(M.difference(N).union(N.difference(M))))
for i in L:
    print i