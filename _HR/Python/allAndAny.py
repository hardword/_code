#!/bin/python
# http://hr.gs/fvq
p, s = raw_input(), raw_input().split()
# palindromic check
print any([p==p[::-1] for p in s]) and len(s)==sum([int(i) > 0 for i in s])

