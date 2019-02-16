#!/bin/python

# XML 1 - Find the Score

import sys
import xml.etree.ElementTree as etree


def get_attr_number(node):
    n = 0
    for _ in node.iter():
        n += len(_.attrib)
    return n


if __name__ == '__main__':
    sys.stdin.readline()
    xml = sys.stdin.read()
    tree = etree.ElementTree(etree.fromstring(xml))
    root = tree.getroot()
    print get_attr_number(root)


# XML 2 - Find the Maximum Depth


maxdepth = 0


def depth(elem, level):
    global maxdepth
    # your code goes here
    level += 1
    if level >= maxdepth:
        maxdepth = level
    for child in elem:
        depth(child, level)  # Need to go deeper on Recursive


if __name__ == '__main__':
    n = int(raw_input())
    xml = ""
    for i in range(n):
        xml = xml + raw_input() + "\n"
    tree = etree.ElementTree(etree.fromstring(xml))
    depth(tree.getroot(), -1)
    print maxdepth
