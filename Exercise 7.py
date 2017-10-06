def log(original_function, logfilename="log.txt"):
    def new_function(*args, **kwargs):
        result = original_function(*args, **kwargs)
        with open("log.txt", "w") as logfile:
            logfile.write("Function '%s' called with positional arguments %s and keyword arguments %s. The result was %s.\n" % (original_function.__name__, args, kwargs, result))
        return result
    return new_function

@log
def sum(a,b):
    return a + b
print(sum(4,3))
with open("log.txt", "w") as logfile:
    print(logfile.read())
