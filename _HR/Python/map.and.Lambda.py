#!/bin/python
# http://hr.gs/eadfcd

cube = lambda x: x**3 # complete the lambda function 

def fibonacci(n):
    # return a list of fibonacci numbers
    result = [0, 1]
    if n == 0:
        result = []
    elif n == 1:
        result = [0]
    else:
        for i in xrange(n-2):
            result.append(result[i]+result[i+1])
    return result    
    
if __name__ == '__main__':
    n = int(raw_input())
    print map(cube, fibonacci(n))