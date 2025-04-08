a = input("First number: ")
b = input("Second number: ")
op = input("Operator: ")
print("You entered:", a, b, op)


# Check if a and b are numbers (integer or float)
if a.replace('.', '', 1).isdigit() and b.replace('.', '', 1).isdigit():
    a = float(a)
    b = float(b)

    if op == '+':
        print("Result:", a + b)
    elif op == '-':
        print("Result:", a - b)
    elif op == '*':
        print("Result:", a * b)
    elif op == '/':
        if b != 0:
            print("Result:", a / b)
        else:
            print("Cannot divide by zero")
    else:
        print("Invalid operator")
else:
    print("Invalid number input")
