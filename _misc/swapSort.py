#!/bin/python

arr=[7,1,3,2,4,5,6]

#not comfortable to use sorted for sorting challenge lol
arr2=sorted(arr)
idtx={v: i for i,v in enumerate(arr)}

swaps = 0

for i,v in enumerate(arr):
    correct_value = arr2[i]
    if v != correct_value:
        to_swap_ix = idtx[correct_value]
        arr[to_swap_ix],arr[i] = arr[i], arr[to_swap_ix]
        idtx[v] = to_swap_ix
        idtx[correct_value] = i
#        print arr
        swaps += 1

#print swaps

#second solution w/o sorted
arr=[7,1,3,2,4,5,6]
#arr=[2,3,4,1,5]

dic_asis={v: i for i,v in enumerate(arr)} #value:index pair
dic_desired={} #index:value pair

for i in xrange(len(arr)):
	idx=0
	for j in xrange(len(arr)):
		#print arr[i], arr[j]
		if arr[i] > arr[j]:
			idx+=1
	dic_desired[idx] = arr[i]

#print dic_asis
#print dic_desired

swaps = 0

for i,v in enumerate(arr):
    correct_v=dic_desired[i]
    if v != correct_v:
        correct_i = dic_asis[correct_v] 
        arr[correct_i], arr[i] = arr[i], arr[correct_i]
        dic_asis[v] = correct_i
        dic_asis[correct_v] = i
        print arr
        swaps += 1

print swaps