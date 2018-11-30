#!/bin/python
# http://hr.gs/e9a

import re

n = int(raw_input())
for i in xrange(n):
    pattern = raw_input()
    try:
        prog = re.compile(pattern)
        print 'True'
    except:
        print 'False'
