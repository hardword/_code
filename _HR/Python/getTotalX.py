#!/bin/python
# http://hr.gs/1jef

from __future__ import print_function

import os

#
# Complete the getTotalX function below.
#

def gcd(a,b):
    """Compute the greatest common divisor of a and b"""
    while b > 0:
        a, b = b, a % b
    return a
    
def lcm(a, b):
    """Compute the lowest common multiple of a and b"""
    return a * b / gcd(a, b)

def getTotalX(a, b):
    c = max(a)
    d = min(b)
    cnt = 1
    result = 0
    while c * cnt <= d:
        test = 0
        for i in a:
            if (c * cnt) % i != 0:
                test += 1
        if test == 0:
            for j in b:
                if j % (c * cnt) != 0:
                    test += 1
        if test == 0:
            result += 1
        cnt += 1
    return result

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    nm = raw_input().split()

    n = int(nm[0])

    m = int(nm[1])

    a = map(int, raw_input().rstrip().split())

    b = map(int, raw_input().rstrip().split())

    total = getTotalX(a, b)

    f.write(str(total) + '\n')

    f.close()