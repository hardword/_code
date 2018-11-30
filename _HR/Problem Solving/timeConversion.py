#!/bin/python
# http://hr.gs/cbecea

from __future__ import print_function

import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    a = s.split(':')
    if 'PM' in a[-1]:
        a[-1] = a[-1].replace('PM','')
        a[0] = str(12+(int(a[0])%12))
    else:
        a[0] = str(int(a[0])%12).zfill(2)
        a[-1] = a[-1].replace('AM','')
    return ':'.join(a)

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = raw_input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()
