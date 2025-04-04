76% of storage used … If you run out of space, you can't save to Drive, back up Google Photos or use Gmail.
# STRING METHODS
# STATEMENTS IN PYTHON
# LOOPS
# BREAK AND CONTINUE

# STRING METHODS

text = "hEllO WoRLD"
# print(text.upper())
# print(text.lower())
# print(text.title())
# # text = text.upper()
# print(text[0:5].upper())
# print(text.capitalize())
# print("Hello! \nHow are you doing today?")
# print(
# """Hello! 
# How are you doing today?""")
greetings = """Hello! 
how are you doing this after?"""
# print(greetings)
text = "hello world"
# print(text.islower())
# print(text.isupper())
# print(text.count("o"))
# print(text.count("l"))
# print(text.count("hello"))
# print(text.count("o", 0, 8))
# print(text.replace("hello", "hi"))
# print(text.replace("e", "a"))

text = "welcome to this class"
# print(text.split())
text = "welcome to this class, have a nice day"
# print(text.split(","))

dayt = "     hello    "
# print(text)
# print(text.strip())


a, b = 4, 7
# print(a+b)

# STATEMENTS IN PYTHON
"""
- CONDITIONAL STATEMENTS
- LOOPING STATEMENTS
"""
"""
if condition:
   # Statements to execute if condition is true
"""
# a = 10
# b = 5
# if a > b:
#     print("a is greater than b")

# if a < b:
#     print("a is greater than b")
# else:
#     print("a is not less than b")

# a = 5
# b = 5
# if a == b:
#     print("they are equal")

# grade = 40

# if grade >= 70:
#     print("you got an A")
# elif grade >= 60 and grade <= 69:
#     print("You got a B")
# elif grade >= 50 and grade <= 59:
#     print("You got a C")
# else:
#     print("Ah you no try")

# LOOPING STATEMENTS
# - WHILE LOOP
"""
while expression:
    statement(s)
"""

# count = 0

# while count < 3:
#     print("Hello")
#     count = count + 1

# while count < 3:
#     print("Hello")
#     count += 1

# count = 5
# while count > 1:
#     print("Hello")
#     count -= 1

#WHILE CONTINUE
# a = 1
# while a < 101:
#     if a % 2 == 0:
#         print(f"{a}: is an even number")
#         a += 1
#         continue
#     print(a)
#     a += 1
    
#WHILE BREAK
# a = 1
# while a < 8:
#     print(a)
#     if a == 4:
#         break
#     a += 1

#WHILE ELSE - IT IS JUST TO AFFIRM THAT THE WHILE LOOP COMPLETED COMPLETELY
# a = 1
# while a < 8:
#     print(a)
#     a += 1
# else:
#     print("we are done")
#     
# WHILE TRUE
# count = 10
# life = True
# while life == True:
#     count -= 1
#     print(f"the current number is {count}")
#     if count == 0:
#         life = False

# foods = ["rice", "eggs", "beans", "spaghetti"] 
foods = ["rice", "eggs", "beans", "spaghetti"]
for b in foods:
    if b == "beans":
        print("That's a nice food")
        continue
    print(b)

# RANGE
# is used to iterate through a number of values using a specified step
for number in range(10):
    print(number)
for number in range(1, 10):
    print(number)
for even_num in range(0, 11, 2):
    print(even_num)
for even_num in range(0, 11, 3):
    print(even_num)

laptops = {
    "laptop1": {
        "name": "HP",
        "model": "Pavilion G6"
}
    }    ,
# foods = ["rice", "eggs", "beans", "spaghetti"] 
foods = ["rice", "eggs", "beans", "spaghetti"]
for b in foods:
    if b == "beans":
        print("That's a nice food")
        continue
    print(b)

# RANGE
# is used to iterate through a number of values using a specified step
for number in range(10):
    print(number)
for number in range(1, 10):
    print(number)
for even_num in range(0, 11, 2):
    print(even_num)
for even_num in range(0, 11, 3):
    print(even_num)

laptops = {
    "laptop1": {
        "name": "HP",
        "model": "Pavilion G6"
    },
}

# The following line was commented out and is not needed
# print(i)
#     print(i)

# foods = ["rice", "eggs", "beans", "spaghetti"] 
# for b in foods:
#     if b == "beans":
#         print("Thats a nice food")
#         continue
#     print(b)

#RANGE
# is used to iterate through a number of values using a specified step
# for number in range(10):
#     print(number)
# for number in range(1,10):
#     print(number)
# for even_num in range(0,11,2):
#     print(even_num)
# for even_num in range(0,11,3):
#     print(even_num)
    

laptops = {
    "laptop1": {
        "name": "HP",
        "model": "Pavilion G6"
    },
    "laptop2": {
        "name": "Dell",
        "model": "Vostro"
    },
    "laptop3": {
        "name": "Lenovo",
        "model": "Thinkpd"
    }
}

for key, value in laptops.items():
    name = value["nIme"]
    model = value["model"]
    print(f"{key}: Name: {name}, Model: {model}")