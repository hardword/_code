#!/bin/python
# https://www.hackerrank.com/domains/python?filters%5Bsubdomains%5D%5B%5D=py-sets

n = int(raw_input())
S = set()

for i in xrange(n):
    e = raw_input()
    S.add(e)

print len(S)


m = int(raw_input())
s = set(map(int, raw_input().split()))
n = int(raw_input())

for i in xrange(n):
    o = raw_input().split()
    cmd = o[0]
    if len(o) == 1:
        eval("s."+cmd+"()")
    else:
        eval("s."+cmd+"("+o[1]+")")
        
print sum(s)

m = int(raw_input())
s = set(map(int, raw_input().split()))
n = int(raw_input())
t = set(map(int, raw_input().split()))

print len(s.union(t))
print len(s.intersection(t))
print len(s.difference(t))
print len(s.symmetric_difference(t))

m = int(raw_input())
s = set(map(int, raw_input().split()))
n = int(raw_input())

for i in xrange(n):
    o = raw_input().split()
    t = set(map(int, raw_input().split()))
    eval("s."+o[0]+"(t)")

print sum(s)


#1
n = int(raw_input())
l = map(int, raw_input().split())
s = set(l)
for i in s:
    if l.count(i) == 1:
        print i


#2
n = int(raw_input())
l = map(int, raw_input().split())
s = set(l)
for i in s:
    l.remove(i)
    try:
        l.remove(i)
    except:
        print i

#3
n = int(raw_input())
l = map(int, raw_input().split())
s = set(l)
print (sum(s)*n-sum(l))/(n-1)



n = int(raw_input())

for i in xrange(n):
    m = int(raw_input())
    s = set(map(int, raw_input().split()))
    l = int(raw_input())
    t = set(map(int, raw_input().split()))
    print len(s-t) == 0


s = set(map(int, raw_input().split()))
n = int(raw_input())
r = True

for i in xrange(n):
    t = set(map(int, raw_input().split()))
    if len(t-s) == 0 and t != s:
        pass
    else:
        r = False
        break

print r