#!/bin/python
# http://hr.gs/ccffef

n = int(raw_input())
# exceptions ==> ['^+.', '^-.', '^.', '.' not in s... ]
for i in xrange(n):
    result = 'False'
    f = ''
    s = raw_input()
    if s[0:2] == '+.' or s[0:2] == '-.':
        s = s.replace('.', '0.')
    if '.' in s:
        try:
            f = float(s)
            result = 'True'
        except:
            pass
    print result
    
