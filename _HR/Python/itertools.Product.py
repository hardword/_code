#!/bin/python
# http://hr.gs/beaffd

from itertools import product

l = map(int, raw_input().split())
m = map(int, raw_input().split())

n = list(product(l,m))
print " ".join(str(t) for t in n)