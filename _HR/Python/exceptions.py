#!/bin/python
# http://hr.gs/fddaaa

n = int(raw_input())

for i in xrange(n):
    try:
        l = map(int, raw_input().split())
        try:
            print l[0]/l[1]
        except Exception, e:
            print "Error Code: "+str(e)
    except Exception, e:
        print "Error Code: "+str(e)
                


