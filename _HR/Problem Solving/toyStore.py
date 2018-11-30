#!/bin/python
# http://hr.gs/16xx

def howManyPurchase(toylist):
    s=set(map(int,toylist.split()))
    p=0
    while True:
        if len(s) == 0:
            break
        else:
            m=min(s)
            ss=set(range(m,m+5))
            s -= ss
            p += 1
    return p

sample='1 3 5 10 17'

print howManyPurchase(sample)