"""
Example of recursion in Python

Pros and cons of recursion:
For large problems with millions of recursive calls you may run out of memory since you'll have millions of open
function calls

Every recursive function can be written as an iterable way. (IT just makes sense to sometimes use one or the other
in some cases)

Pros/Cons:
Con: does not scale up like iteration. Requires more memory
Con: many languages have iterative solutions be faster than recursive solutions
Cons: sometimes harder to understand than iterative solution

Pro: in some cases it is extremely fast and easy to code. ex: tree traversals and binary search.

"""


def getFactorial(n):
    if n < 2:
        return 1
    else:
        return n * getFactorial(n-1)


print(getFactorial(5))
