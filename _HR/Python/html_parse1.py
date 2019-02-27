#!/bin/python

# HTML Parser - Part 1

from HTMLParser import HTMLParser


class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print "Start :", tag
        if attrs:
            for _ in attrs:
                print "->", _[0], ">", _[1]

    def handle_endtag(self, tag):
        print "End   :", tag

    def handle_startendtag(self, tag, attrs):
        print "Empty :", tag
        if attrs:
            for _ in attrs:
                print "->", _[0], ">", _[1]


n = int(raw_input())
html = ""
for _ in xrange(n):
    html += raw_input()

parser = MyHTMLParser()
parser.feed(html)
