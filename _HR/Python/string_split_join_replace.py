#!/bin/python
# python string split, join and replace

def split_and_join(line):
    l = line.rstrip().split()
    return "-".join(l)

def why_not_replace(line):
    return line.replace(' ', '-')
	

if __name__ == '__main__':
    line = raw_input()
    result = split_and_join(line)
    print result