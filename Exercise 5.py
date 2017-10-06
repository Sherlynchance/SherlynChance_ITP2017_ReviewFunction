ADD, SUB, MUL, DIV = range(4)
def calculator (num1, num2, operation = ADD, output_format=float):
    if operation == ADD:
        result = num1 + num2
    elif operation == SUB:
        result = num1 - num2
    elif operation == MUL:
        result = num1 * num2
    elif operation == DIV:
        result = num1 / num2
    else:
        raise ValueError
    if output_format == float:
        result = float(result)
    elif output_format == int:
        result = round(result)
    return result
print(calculator(2,3.0))
print(calculator(2,3.0, output_format=int))
print(calculator(2,3.0,operation=DIV))
print(calculator(2,3.0, operation=DIV, output_format=int))
