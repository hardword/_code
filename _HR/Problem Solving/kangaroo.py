#!/bin/python
# http://hr.gs/dafbcf

import os

# Complete the kangaroo function below.
def kangaroo(x1, v1, x2, v2):
    cnt = 1
    gap1 = x2 - x1
    result = ''
    while True:
        p1 = x1 + (cnt * v1)
        p2 = x2 + (cnt * v2)
        gap2 = p2 - p1
        if p1 == p2:
            result = 'YES'
            break
        elif gap2 >= gap1:
            result = 'NO'
            break
        elif gap2 < 0: 
            result = 'NO'
            break
        cnt += 1
        gap1 = gap2
    return result
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    x1V1X2V2 = raw_input().split()

    x1 = int(x1V1X2V2[0])

    v1 = int(x1V1X2V2[1])

    x2 = int(x1V1X2V2[2])

    v2 = int(x1V1X2V2[3])

    result = kangaroo(x1, v1, x2, v2)

    fptr.write(result + '\n')

    fptr.close()