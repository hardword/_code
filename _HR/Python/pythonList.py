#!/bin/python
# http://hr.gs/dg2 

if __name__ == '__main__':
    N = int(raw_input())
    l = []
    for i in xrange(N):
        inst = raw_input().rstrip().split()
        if inst[0] == 'insert':
            l.insert(int(inst[1]),int(inst[2]))
        elif inst[0] == 'print':
            print l
        elif inst[0] == 'remove':
            l.remove(int(inst[1]))
        elif inst[0] == 'append':
            l.append(int(inst[1]))
        elif inst[0] == 'sort':
            l.sort()
        elif inst[0] == 'pop':
            l.pop()
        elif inst[0] == 'reverse':
            l.reverse()
        #print "inst: ", inst
        #print "list: ", l
    
    # with eval()    
    n = int(raw_input())
    l = []
    for _ in range(n):
        s = raw_input().split()
        cmd = s[0]
        args = s[1:]
        if cmd !="print":
            cmd += "("+ ",".join(args) +")"
            eval("l."+cmd)
        else:
            print l