#!/bin/python
# http://hr.gs/v6h

def merge_the_tools(string, k):
    for i in xrange(len(string)/k):
        ustring=''
        for c in string[i*k:i*k+k]:
            if c in ustring:
                pass
            else:
                ustring += c
        print ustring
