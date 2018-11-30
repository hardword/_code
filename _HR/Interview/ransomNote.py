#!/bin/python
# http://hr.gs/16xx

ms = 'give me one grand today night'
ns = 'give one grand today f'

magazine = ms.split()
note = ns.split()

md = {x:magazine.count(x) for x in magazine}
result = 'Yes'

for w in note:
	if w in magazine:
		md[w] = md[w] - 1
		if md[w] < 0:
			result = "No"
			break
	else:
		result = "No"
		break

print result

result = 'Yes'

for w in note:
	try:
	   magazine.remove(w)
	except:
	   result = "No"

print result

ms = 'give me one one one grand today night'
ns = 'give one grand today f'

magazine = ms.split()
note = ns.split()


from collections import Counter

result = "Yes"
print Counter(note)
print Counter(magazine)

comp = (Counter(note) - Counter(magazine))
print comp
if comp != {}:
	result = "No"

print result