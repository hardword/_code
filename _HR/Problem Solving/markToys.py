#!/bin/python
# http://hr.gs/fdccad

import os

# Complete the maximumToys function below.
def maximumToys(prices, k):
    cnt=0
    ts=0
    prices.sort()
    for i in prices:
        ts += i
        if ts <= k:
            cnt += 1
        else:
            break
    return cnt

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = raw_input().split()

    n = int(nk[0])

    k = int(nk[1])

    prices = map(int, raw_input().rstrip().split())

    result = maximumToys(prices, k)

    fptr.write(str(result) + '\n')

    fptr.close()