#!/bin/python

# Validating phone numbers

import re

n = int(raw_input())

for _ in xrange(n):
    s = raw_input()
    match = re.search(r'^[789][0-9]{9}$', s)
    if match:
        print 'YES'
    else:
        print 'NO'

# Validating and Parsing Email Addresses
# suggestion: "import email.utils" to complete this challenge

email_pattern = r"^<[A-Za-z](\w|-|\.|_)+@[A-Za-z]+\.[A-Za-z]{1,3}>$"
for _ in range(n):
    name, email = raw_input().split()
    if re.match(email_pattern, email):
        print name, email


# Hex Color Code

p = r"(?<!^)(#(?:[\dA-Fa-f]{3}){1,2})"

# (?<!^)(# means not match the start of each line -> exclude comment
# https://www.regular-expressions.info/refadv.html
# (?:[\dA-Fa-f]{3}){1,2}): non-capturing group
# https://www.regular-expressions.info/refcapture.html

for i in xrange(int(raw_input())):
    for j in re.findall(p, raw_input()):
        print j


# Validating Roman Numerals

regex_pattern = r"M{0,3}(C[MD]|D?C{0,3})(X[CL]|L?X{0,3})(I[VX]|V?I{0,3})$"

# https://developers.google.com/edu/python/regular-expressions

print(str(bool(re.match(regex_pattern, raw_input()))))
