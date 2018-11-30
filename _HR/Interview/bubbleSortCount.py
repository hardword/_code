#!/bin/python
# http://hr.gs/16xx

# bubble sort counting

def countSwaps(a):
    n = len(a)
    cnt=0
    for i in xrange(n):
        for j in xrange(n-1):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
                cnt += 1
    print "Array is sorted in "+str(cnt)+" swaps."
    print "First Element: "+str(a[0])
    print "Last Element: "+str(a[n-1])

a=[4,2,3,1]
countSwaps(a)