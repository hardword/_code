#!/bin/python
# http://hr.gs/fnu

import os

# Complete the twoStrings function below.
def twoStrings(s1, s2):
    answer = 'NO'
    s1 = sorted(set(s1))
    s2 = sorted(set(s2))
    s = s1 if len(s1) < len(s2) else s2
    t = s1 if len(s1) >= len(s2) else s2
    for i in xrange(len(s)):
        if s[i] in t:
            answer = 'YES'
            break
    return answer

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(raw_input())

    for q_itr in xrange(q):
        s1 = raw_input()

        s2 = raw_input()

        result = twoStrings(s1, s2)

        fptr.write(result + '\n')

    fptr.close()