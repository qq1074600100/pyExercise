import math
import functools


def quadratic(a, b, c):
    tmp = b**2-4*a*c
    tmp = math.sqrt(tmp)
    x1 = (-b+tmp)/(2*a)
    x2 = (-b-tmp)/(2*a)
    return x1, x2


def my_abs(x):
    if(x < 0):
        x = -x
    return x


def product(x, y=1, *args):
    result = x*y
    for arg in args:
        result = result*arg
    return result


def move(n, a, b, c):
    if n == 1:
        print(a, '-->', c)
    else:
        move(n-1, a, c, b)
        print(a, '-->', c)
        move(n-1, b, a, c)


def findMinAndMax(L):
    min = None
    max = None
    for x in L:
        if min == None or min > x:
            min = x
        if max == None or max < x:
            max = x
    return (min, max)


def triangles(max):
    n = 2
    tmpL = [1]
    yield tmpL
    while n < max:
        rstL = [1, 1]
        for x in range(n-2):
            rstL.insert(x+1, tmpL[x]+tmpL[x+1])
        tmpL = rstL
        yield tmpL
        n = n+1


def add(x, y, fun):
    return fun(x)+fun(y)


def powerN(x, n):
    sum = 1
    for i in range(n):
        sum = sum*x
    return sum


def normalize(name):
    name = str.lower(name)
    return name.capitalize()


def prod(L):
    def cheng(a, b):
        return a*b
    return functools.reduce(cheng, L)


def char2num(s):
    digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4,
              '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '.': '.'}
    return digits[s]


def fn(x, y):
    return x * 10 + y


def str2float(s):
    fields = str.split(s, '.')
    L1 = list(map(char2num, fields[0]))
    L2 = list(map(char2num, fields[1]))
    num1 = functools.reduce(fn, L1)
    num2 = functools.reduce(fn, L2)/powerN(10, len(L2))
    rst = num1+num2
    return rst


def _odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n


def _not_divisible(n):
    return lambda x: x % n > 0


def primes():
    yield 2
    it = _odd_iter()
    while True:
        n = next(it)
        yield n
        it = filter(_not_divisible(n), it)


def is_palindrome(n):
    L = list(str(n))
    length = len(L)
    i = 0
    while i < length/2:
        if L[i] != L[length-i-1]:
            return False
        i = i+1
    return True
