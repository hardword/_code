#!/bin/python

# Standardize Mobile Number Using Decorators


def wrapper(f):
    def fun(l):
        # complete the function
        formatted = ["+91 "+_[-10:-5]+" "+_[-5:] for _ in l]
        f(formatted)
    return fun


@wrapper
def sort_phone(l):
    print '\n'.join(sorted(l))


if __name__ == '__main__':
    l = [raw_input() for _ in range(int(input()))]
    sort_phone(l)


# Decorators 2 - Name Directory

def person_lister(f):
    def inner(people):
        # complete the function
        return map(f, sorted(people, key=lambda person: int(person[2])))
    return inner


@person_lister
def name_format(person):
    return ("Mr. " if person[3] == "M" else "Ms. ") + person[0] + " " + person[1]


if __name__ == '__main__':
    people = [raw_input().split() for i in range(int(raw_input()))]
    print '\n'.join(name_format(people))
