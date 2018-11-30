#!/bin/python
# http://hr.gs/ea0

a = [1,2,3,4,5]
n = len(a)

d = 4 #Left Rotation

b = a[d-n:]+a[:d]
    
print " ".join(map(str, b))