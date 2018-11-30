#!/bin/python
# http://hr.gs/cddafc

from collections import defaultdict

def isValid(s):
    d = defaultdict(int)
    for c in s:
        d[c] += 1
    l = d.values()
    #print d, l
    result = "NO"
    maxl, minl = max(l), min(l)
    #print maxl, minl
    if maxl == minl:
        result = "YES"
    elif len(set(l)) == 2:
        maxlc, minlc = l.count(maxl), l.count(minl)
        if maxlc == 1 and maxl - 1 == minl:
            result = "YES"
        elif minlc ==1 and minl == 1:
            result = "YES"
    return result

print isValid('aabbc')

