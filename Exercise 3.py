import  math
def hypotenuse (a,b):
    try:
        return math.sqrt((a ** 2) + (b ** 2))
    except TypeError:
        return None
print(hypotenuse(2,5))
print(hypotenuse("3","5"))
print(hypotenuse(6,"4"))
