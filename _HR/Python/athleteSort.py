#!/bin/python

if __name__ == '__main__':
    nm = raw_input().split()

    n = int(nm[0])

    m = int(nm[1])

    arr = []

    for _ in xrange(n):
        arr.append(map(int, raw_input().rstrip().split()))

    k = int(raw_input())

krr = zip(*arr)[k]
# sorted index list
# https://stackoverflow.com/questions/7851077/how-to-return-index-of-a-sorted-list
srr = sorted(range(len(krr)), key=lambda i: krr[i])
for i in srr:
    print ' '.join(str(j) for j in arr[i])