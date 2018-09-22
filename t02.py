def calc(a, opr, b):
    if opr == '+':
        return a + b
    elif opr == '-':
        return a - b
    elif opr == '*':
        return a * b
    elif opr == '/':
        try:
            return a / b
        except ZeroDivisionError:
            return "Division by zero"
    else:
        return 'Not found operation'


x1, op, x2 = input("Input your example: ").split()
print(calc(float(x1), op, float(x2)), end='')
