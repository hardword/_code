#!/usr/bin/env python

# http://hr.gs/ccfbdb
# https://en.wikipedia.org/wiki/Lexicographical_order
# https://www.nayuki.io/page/next-lexicographical-permutation-algorithm

input=['bbfdgstgggggddssddeeedd', 'akdb', 'fedcbabcd', 'dcbb']

arr=list(input[2])
# Find non-increasing suffix
i = len(arr)-1
while i > 0 and arr[i-1] >= arr[i]:
	i -= 1
if i <= 0:
	print "no answer"

# Find successor to pivot
j = len(arr)-1
while arr[j] <= arr[i - 1]:
		j -= 1
arr[i - 1], arr[j] = arr[j], arr[i - 1]
	
# Reverse suffix
arr[i : ] = arr[len(arr) - 1 : i - 1 : -1]

print ''.join(arr)


# Things I learned

import itertools
## string to list
lst = list(input[0])
#print lst

## sorting a list
lst = sorted(lst)

## sorting a list in a reverse order
lst = sorted(lst, reverse=True)

## with unique values
lst = sorted(set(lst), reverse=True)

## make list of serial numbers
lst2 = range(1,5)

## permutation, combination of the list
lst2 = list(itertools.permutations(range(1,5)))
lst2 = list(itertools.combinations(range(1,5), len(range(1,5))-2))
## need to learn itertools a little more

## merge list
lst += range(10)
lst = lst + lst2

## swap values in a list
lst[0], lst[9] = lst[9], lst[0]

## list to string
s=''.join(str(_) for _ in lst)
t=''.join(map(str, lst))

## reverse array
# print lst
lst[0:] = lst[len(lst)-1::-1]
# print lst