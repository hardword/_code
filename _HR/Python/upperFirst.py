#!/bin/python
# http://hr.gs/foh

s = 'hello   world  lol'
s = '1 2 2 3 4 5 6 7 8  9'

L = list(s)
L[0] = L[0].upper()
for i in xrange(1, len(L)):
    if L[i-1] == ' ':
        L[i] = L[i].upper()        
print "".join(L)
