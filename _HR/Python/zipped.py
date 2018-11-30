#!/bin/python
# http://hr.gs/dacbdf

n = map(int, raw_input().split())

l = []
for subject in xrange(n[1]):
	l.append(map(float, raw_input().split()))


avg = [sum(col)/len(col) for col in zip(*l)]

for a in avg:
	print a


	