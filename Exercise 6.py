ADD, SUB, MUL, DIV = range(4)
def calculator (operation=ADD, output_format=float, *args):
    result = args[0]
    if len(args) < 2:
        raise ValueError
    for x in args[1:]:
        if operation == ADD:
            result += x
        elif operation == SUB:
            result -= x
        elif operation == MUL:
            result *= x
        elif operation == DIV:
            result /= x
        else:
            raise ValueError
        if output_format == float:
            result = float(result)
        elif output_format == int:
            result = round(result)
        else:
            raise ValueError
    return result
print(calculator(MUL, int, 5, 5, 5))
print(calculator(ADD, int, 5, 5, 5))
print(calculator(SUB, int, 20, 5, 1))
print(calculator(DIV, float, 20, 5))

