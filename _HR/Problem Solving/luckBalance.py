#!/bin/python
# http://hr.gs/cfcbff

# Complete the luckBalance function below.
def luckBalance(k, contests):
    a, b = [], []
    for c in contests:
        if c[1] == 1:
            a.append(c[0])
        else:
            b.append(c[0])
    a = sorted(a, reverse = True)
    return sum(a[:k])-sum(a[k:])+sum(b)
    

if __name__ == '__main__':
    
    k = 3
    
    contests = [[5, 1], [2, 1], [1, 1], [8, 1], [10, 0], [5, 0]]

    result = luckBalance(k, contests)

    print result