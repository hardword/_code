#!/bin/python
# http://hr.gs/fcg

import calendar
w={0: 'MONDAY', 1: 'TUESDAY', 2: 'WEDNESDAY', 3: 'THURSDAY', 4: 'FRIDAY', 5: 'SATURDAY', 6: 'SUNDAY'}

a=map(int, raw_input().split())
b=calendar.weekday(a[2], a[0], a[1])

print w[b]
