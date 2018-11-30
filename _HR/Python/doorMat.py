#!/bin/python
# http://hr.gs/duo

h = 7
w = 21

p1 = '-'
p2 = '.|.'
p3 = 'WELCOME'

z=[]

for i in range(1, h, 2):
	l = len(p2*i)
	m = (w-l)/2
	z.append(p1*m+p2*i+p1*m)

print "\n".join(z)
print p1*((w-7)/2)+p3+p1*((w-7)/2)
z.reverse()
print "\n".join(z)


	
	