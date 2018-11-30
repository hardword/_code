#!/bin/python
# http://hr.gs/babead

def isBalanced(s):
    result="YES"
    bd={'}':'{',']':'[',')':'('}
    bl=[]    
    for b in s:
        if b in '{[(':
            bl.append(b)
        elif len(bl) == 0 and b in '}])':
            result = "NO"
            break
        elif bl[-1] == bd[b]:
            bl.pop()
        else:
            result = "NO"
            break
    if len(bl) !=0:
        result = "NO"
    return result

s = '{{}}[][](())'
print isBalanced(s)