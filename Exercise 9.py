def generator(n):
    while n > 0:
        yield n
        n -= 1
for x in generator(10):
    print(x)
