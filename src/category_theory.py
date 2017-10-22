import random

def comp(f, g):
    return lambda x: g(f(x))

# f: A -> B
# memoize returns a new function, f': A -B
# that's almost like f except it also caches its results
def memoize(f):
    cache = {}
    func = f
    def wrapper(a):
        cached = cache.get(a)
        if cached is not None:
            return cached
        val = func(a)
        cache[a] = val
        return val
    return wrapper

def randgen(seed):
    random.seed(seed)
    return random.random()

def boolean_id(b):
    return b

def boolean_neg(b):
    return not b

def boolean_absurdity_1(b):
    return True

def boolean_absurdity_2(b):
    return False

def factorial(n):
    if n <= 1:
        return 1
    acc = 1
    for i in range(0, n):
        acc *= i+1
    return acc
