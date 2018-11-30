#!/bin/python
# http://hr.gs/babead

def isBalanced(list):
    """Validate if an input string is having balanced bracket pairs."""
    brackets_pair={'(':')', '[':']', '{':'}'}
    for i in list:
        if (len(i) / 2) * 2 != len(i):
            print False
        elif i[0] in brackets_pair.values() or i[-1] in brackets_pair.keys():
            print False
        else:
            stack = []
            res = True
            for j in i:
                if j in brackets_pair.keys():
                    stack.append(j)
                elif len(stack) != 0 and j == brackets_pair[stack[-1]]:
                    stack.pop()
                else:
                    res = False
            print res

testcases = ["[{}]()", "[{]}", "}()[]{}}", "[]{()}][", "[[[[[[]]]]]]", "[[{{]]}}[]]", "[[[}}}", "{{{{{[{]}}}}}}"]

isBalanced(testcases)
