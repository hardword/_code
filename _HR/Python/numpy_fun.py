#!/bin/python
import numpy

arr = [5, 4, 3, 0, -1, -10]

def arrays(arr):
	#as float value in a reverse order
	return numpy.array(arr, float)[::-1]

def reshape(arr, row = 3, column = 2):
	new_arr = numpy.array(arr)
	return numpy.reshape(new_arr,(row,column))

print arrays(arr), reshape(arr)

arr = [[2,3,4], [-2,-3,-4]]

def transpose(arr):
	return numpy.transpose(numpy.array(arr))

def flatten(arr):
	numpy.array(default_list).flatten()

print arrays(arr), reshape(arr)

default_list1 = [[1, 2], [1, 2], [1, 2], [1, 2]]
default_list2 = [[3, 4], [3, 4], [3, 4]]

array1 = numpy.array(default_list1)
array2 = numpy.array(default_list2)

print numpy.concatenate((array1, array2), axis = 0)
#print numpy.concatenate((array1, array2), axis = 1)

