#!/usr/bin/env python

# http://hr.gs/abbdcb

#sample=['1 1 1 0 0 0', '0 1 0 0 0 0', '1 1 1 0 0 0', '0 0 2 4 4 0', '0 0 0 2 0 0', '0 0 1 2 4 0']
sample=['-9 -9 -9  1 1 1', '0 -9  0  4 3 2', '-9 -9 -9  1 2 3', '0  0  8  6 6 0', '0  0  0 -2 0 0', '0  0  1  2 4 0']

arr=[]

for i in xrange(6):
    arr.append(map(int, sample[i].rstrip().split()))

result=-100

for x in xrange(4):
	for y in xrange(4):
		hg=arr[x][y:y+3]+arr[x+2][y:y+3]
		hg.append(arr[x+1][y+1])
		if sum(hg) > result:
			result = sum(hg)

print result