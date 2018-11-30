#!/bin/python
# http://hr.gs/2r2s

import os

# Complete the breakingRecords function below.
def breakingRecords(scores):
    result = [0, 0]
    minimum = scores[0]
    maximum = scores[0]
    
    for i in xrange(1, len(scores)):
        if scores[i] < minimum:
            result[1] += 1
            minimum = scores[i]
        elif scores[i] > maximum:
            result[0] += 1
            maximum = scores[i]
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(raw_input())

    scores = map(int, raw_input().rstrip().split())

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
