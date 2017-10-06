def factorial (n):
    try:
        if n == 1:
            return 1
        else:
            return (n * factorial(n-1))
    except (RecursionError, TypeError):
        return None
print(factorial(5))
