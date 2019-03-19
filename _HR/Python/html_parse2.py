#!/bin/python

# HTML Parser - Part 2

from HTMLParser import HTMLParser


class MyHTMLParser(HTMLParser):
    def handle_comment(self, data):
        if "\n" in data:
            print ">>> Multi-line Comment\n"+data
        else:
            print ">>> Single-line Comment\n"+data

    def handle_data(self, data):
        if "\n" == data:
            pass
        else:
            print ">>> Data\n"+data


html = ""
for i in range(int(raw_input())):
    html += raw_input().rstrip()
    html += '\n'

parser = MyHTMLParser()
parser.feed(html)
parser.close()
