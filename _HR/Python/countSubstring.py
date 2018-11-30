#!/bin/python
# http://hr.gs/ecdeed

def count_substring(string, sub_string):
    c = 0
    if sub_string in string:
        i = string.find(sub_string)
        c = 1
        n = len(sub_string)
        while i != -1:
            i = string.find(sub_string,i+1)
            if i != -1:
                c += 1
    return c

def count_substring2(string, substring):
    return sum([ 1 for i in range(len(string)-len(substring)+1) if string[i:i+len(substring)] == substring])

s = 'ABCDCDC'
ss = 'CDC'

print count_substring(s, ss)
print count_substring2(s, ss)