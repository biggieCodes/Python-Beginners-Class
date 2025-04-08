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

    
    
    
    #if and else and elif statements
     
    if operator == '+':
        result: float = num1 + num2
    elif operator == "-":
        result: float = num1 - num2
    elif operator == '*':
        result: float = num1 * num2
    elif operator == '/':
        result: float = num1 / num2
    else:
        print("Invalid operator") 
#     print("Invalid input")
    print("Result:", result)
# else:



     
