a = input("First number: ")
b = input("Second number: ")
op = input("Operator (+, -, *, /): ")

if a.replace('.', '', 1).isdigit() and b.replace('.', '', 1).isdigit():
    a = float(a)
    b = float(b)
    if op == '+':
        print(a + b)
    elif op == '-':
        print(a - b)
    elif op == '*':
        print(a * b)
    elif op == '/':
        if b != 0:
            print(a / b)
        else:
            print("Can't divide by zero")
    else:
        print("Invalid operator")
else:
    print("Invalid input")
a = input("First number: ")
b = input("Second number: ")
op = input("Operator (+, -, *, /): ")

if a.replace('.', '', 1).isdigit() and b.replace('.', '', 1).isdigit():
    a = float(a)
    b = float(b)
    if op == '+':
        print(a + b)
    elif op == '-':
        print(a - b)
    elif op == '*':
        print(a * b)
    elif op == '/':
        if b != 0:
            print(a / b)
        else:
            print("Error: Division by zero is not allowed.")
    else:
        print("Error: Invalid operator.")
else:
    print("Error: Invalid input. Please enter numeric values.")