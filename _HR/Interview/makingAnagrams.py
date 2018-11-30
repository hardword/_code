#!/bin/python
# http://hr.gs/16xx

from collections import defaultdict

def makeAnagram(a, b):
    c, d =list(a), list(b)
    e = defaultdict(int)
    result = 0
    for i in c:
        e[i] += 1
    for j in d:
        e[j] -= 1
    for k in e:
        result += abs(e[k])
    return e

a='showman'
b='woman'

print makeAnagram(a,b)