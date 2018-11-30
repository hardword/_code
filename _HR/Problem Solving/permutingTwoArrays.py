#!/bin/python
# http://hr.gs/abbbca

import os
# Complete the twoArrays function below.
def twoArrays(k, A, B):
    A = sorted(A)
    B = sorted(B, reverse=True)
    result = "YES"
    for i in xrange(len(A)):
        if A[i] + B[i] < k:
            result = "NO"
            break
    return result
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(raw_input())

    for q_itr in xrange(q):
        nk = raw_input().split()

        n = int(nk[0])

        k = int(nk[1])

        A = map(int, raw_input().rstrip().split())

        B = map(int, raw_input().rstrip().split())

        result = twoArrays(k, A, B)

        fptr.write(result + '\n')

    fptr.close()
