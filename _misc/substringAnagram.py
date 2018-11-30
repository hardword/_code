#!/bin/python

import collections

def get_all_substrings(str, length):
    if length == 1:
        l=list(str)
    else:
        l=[]
        for i in xrange(len(str)+1):
            if i+length <= len(str):
                substr=str[i:i+length]
                l.append(substr)
    return l

def isAnagram(s1, s2): 
    l1, l2 = list(s1), list(s2) 
    counts=collections.defaultdict(int) 
    for l in l1: 
        counts[l]+=1 
    for l in l2: 
        counts[l]-=1 
        if counts[l]<0: 
            return False 
    return True

case=int(raw_input())
for i in xrange(case):
    str=raw_input()
    cnt=0
    for j in xrange(1, len(str)):
        substr=get_all_substrings(str, j)
        idx=0
        for k in substr:
            idx+=1
            if idx < len(substr):
                for l in substr[idx:]:
                    if isAnagram(k, l):
                        cnt+=1 
    print cnt
    
