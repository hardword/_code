#!/bin/python
import numpy

#for HR compatibility
numpy.set_printoptions(legacy='1.13')

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

l = [5, 7]
print numpy.eye(l[0], l[1], k=1)
print str(numpy.eye(l[0], l[1])).replace('1', ' 1').replace('0', ' 0')

print numpy.eye(l[0], l[1], k=1)
print str(numpy.eye(l[0], l[1])).replace('1', ' 1').replace('0', ' 0')

print numpy.identity(l[0])

t =tuple(l)
print numpy.zeros(t, dtype = numpy.int)
print numpy.ones(t, dtype = numpy.int)


my_array = [1.1, 2.2, 3.3, 4.4, 5.5, 6.6, 7.7, 8.8, 9.9]
my_array = numpy.array(my_array)

numpy.set_printoptions(sign=' ')

print numpy.floor(my_array)
print numpy.ceil(my_array)
print numpy.rint(my_array)

my_array = numpy.array([ [1, 2], [3, 4] ])

print numpy.mean(my_array, axis = 0)        #Output : [ 2.  3.]
print numpy.mean(my_array, axis = 1)        #Output : [ 1.5  3.5]
print numpy.mean(my_array, axis = None)     #Output : 2.5
print numpy.mean(my_array)                  #Output : 2.5

print numpy.var(my_array, axis = 0)         #Output : [ 1.  1.]
print numpy.var(my_array, axis = 1)         #Output : [ 0.25  0.25]
print numpy.var(my_array, axis = None)      #Output : 1.25
print numpy.var(my_array)                   #Output : 1.25

print numpy.std(my_array, axis = 0)         #Output : [ 1.  1.]
print numpy.std(my_array, axis = 1)         #Output : [ 0.5  0.5]
print numpy.std(my_array, axis = None)      #Output : 1.11803398875
print numpy.std(my_array)                   #Output : 1.11803398875