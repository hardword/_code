#!/bin/python
# http://hr.gs/fefbd

def swap_case(s):
    sf = ''
    for c in s:
        if c.isupper():
            sf += c.lower()
        else:
            sf += c.upper()
    return sf

if __name__ == '__main__':
    s = raw_input()
    result = swap_case(s)
    print result