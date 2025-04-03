# this is a comment

"""
this is also another form of comment
"""

'''
this is also another comment
'''
# print("call 911")


# DATA TYPES
#STRING
greet = "hello world"
#print(greet)

#INTEGER
a = 22
#print(a)

#FLOAT
ab = 1.567
# print(ab)

#BOOL
my_decision = True
# print(my_decision)

# PYTHON LISTS
shopping_list = ["rice", "books", "pen"]
# print(shopping_list)
shopping_list2 = ["rice", 200, "pen", False]
# print(shopping_list2)

#TUPLES
cordinates = (1.228888, 1.999999, "east")
# print(cordinates)

greet = "Good morning"
# print(greet)

a = 1
# print(a)

#STRING FORMATTING
print(greet, a)
# print(greet + a) # NOTE THAT THIS DOES NOT WORK WHEN COMBINING STRINGS AND INTEGERS TOGETHER
greetings = f"Hello {greet} {a}, How was your night?"
print(greetings)

#INPUT AND OUPUT
# name = input("What is your name? ")
# print(name)

# age = input("How old are you? ")
# print(f"Hello {name}, You are now {age} years old")

#PYTHON OPERATORS
'''
ARITHMETIC OPERATORS
LOGICAL OPERATORS
'''
# ARITHMETIC OPERATORS: + - * ** / // %
# ASSIGNMENT OPRATORS: = == != += -= < > <= >= 
# LOGICAL OPERATORS: and or not

#examples
a = 2
b = 4
c = a + b
print(c)
d = a // b #round off
print(d)
e = a ** b # raised to power
print(e)
f = b % 3 # modulus
print(f)
print(a == b)
g = 0.5
print(type(a))
print(type(g))

decision = False
print(type(decision))

#converting to various datatypes
number = "1.5"
print(type(number))
number = float(number)
print(type(number))

# age = int(input("How old are you? "))
# print(f"You are now {age} years old")
# print(type(age))

age = input("How old are you? ")
age = int(age)
print(type(age))