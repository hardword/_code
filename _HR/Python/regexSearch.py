#!/bin/python

# Validating phone numbers

from itertools import groupby
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


# Validating UID

n = int(raw_input())

for _ in xrange(n):
    uid = raw_input()
    if len(uid) == 10 or uid.isalnum():
        if len(re.findall(r'[A-Z]', uid)) < 2:
            print "Invalid"
        elif len(re.findall(r'[0-9]', uid)) < 3:
            print "Invalid"
        elif len(list(uid)) != len(set(uid)):
            print "Invalid"
        else:
            print "Valid"
    else:
        print "Invalid"

# Validating Credit Card Numbers


def validate(cn):
    p = r"^[4-6][0-9]{3}[-]{0,1}[0-9]{4}[-]{0,1}[0-9]{4}[-]{0,1}[0-9]{4}$"
    result = False
    if re.match(p, cn):
        result = True
        cn = cn.replace("-", "")
        groups = groupby(cn)
        for digit, group in groups:
            if sum(1 for _ in group) >= 4:
                print digit, group
                result = False
                break
    return result


n = int(raw_input())

for _ in xrange(n):
    cn = raw_input()
    if validate(cn):
        print "Valid"
    else:
        print "Invalid"

# Matrix Script

nm = raw_input().split()
n = int(nm[0])
m = int(nm[1])
matrix = []

for _ in xrange(n):
    matrix_item = raw_input()
    matrix.append(matrix_item)

s = ''.join(matrix[i][j] for j in range(m) for i in range(n))

# \w ==>      alphanumeric (low ascii) & underscore. Equivalent to [A-Za-z0-9_]
# (?<=\w) ==> Positive Look Behind, Negative : '!' instead of '='
# (?=\w) ==>  Positive Look Ahead, Negative : '!' instead of '='

print re.sub(r"(?<=\w)([^\w]+)(?=\w)", " ", s)


# Validating Postal Codes

regex_integer_in_range = r"^[1-9][0-9]{5}$"  # 6 digits not starting with 0
# alternating repetitive digit pair check
regex_alternating_repetitive_digit_pair = r"(.)(?=.\1)"

# (.)     => greoup 1
# (?=     => Positive Lookahead, negative look ahead : '!' instead of '='
# .\1)    => any chr + group1

# Regex Substitution

# lambda for group
re.sub(r'(?<= )(&&|\|\|)(?= )', lambda x: 'and' if x.group()
       == '&&' else 'or', raw_input())

# Re.start() & Re.end()

s = "aaadaa"
t = "aa"
p = re.compile(t)
# search: first location where the regular expression pattern produces a match
r = p.search(s)

if not r:
    print "(-1, -1)"
while r:
    print (r.start(), r.end() - 1)
    r = p.search(s, r.start() + 1)
