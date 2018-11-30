#!/bin/python
# http://hr.gs/fn1

def print_formatted(number):
    w = len(bin(number)[2:])
    for i in xrange(1,number+1):
        print str(i).rjust(w), oct(i)[1:].rjust(w), hex(i)[2:].upper().rjust(w), bin(i)[2:].rjust(w)

if __name__ == '__main__':
    n = int(raw_input())
    print_formatted(n)