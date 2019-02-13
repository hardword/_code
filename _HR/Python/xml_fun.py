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
