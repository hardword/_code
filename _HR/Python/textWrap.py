#!/bin/python
# http://hr.gs/cbbdaf

import textwrap

def wrap(string, max_width):
    result = textwrap.wrap(string,max_width)
    return "\n".join(result)

if __name__ == '__main__':
    string, max_width = raw_input(), int(raw_input())
    result = wrap(string, max_width)
    print result