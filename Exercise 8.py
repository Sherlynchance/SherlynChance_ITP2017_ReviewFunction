import math
lam1 = lambda a: a**2
lam2 = lambda b,c: math.sqrt(b**2 + c**2)
lam3 = lambda *args: sum(args) /len(args)
lam4 = lambda d: "".join(set(d))
def first(a):
    return a**2
def second(b,c):
    return math.sqrt(b**2 + c**2)
def third(*args):
    return sum(args) /len(args)
def fourth(d):
    return "".join(set(d))
print(first(4))
print(second(10,3))
print(third(4,5,6,7))
print(fourth('qwerqwer'))

