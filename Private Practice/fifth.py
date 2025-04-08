#f_strings


name = "Chuka"
age = 25

print(f"My name is {name} and I am {age} years old.")


# f-strings are a way to format strings in Python, allowing you to embed expressions inside string literals, using curly braces {}.
# f-strings are prefixed with the letter 'f' or 'F'.
# They are evaluated at runtime and can contain any valid Python expression.
# f-strings are more readable and concise compared to the older string formatting methods like % formatting or str.format().
# f-strings are also faster than the older methods because they are evaluated at runtime and do not require additional function calls.
# Example of using f-strings with expressions
x = 10
y = 5
result = f"The sum of {x} and {y} is {x + y}."
print(result)
# Example of using f-strings with dictionaries
person = {"name": "Alice", "age": 30}
info = f"My name is {person['name']} and I am {person['age']} years old."   
print(info)


# Example of using f-strings with lists 
fruits = ["apple", "banana", "cherry"]
fruit_list = f"My favorite fruits are: {', '.join(fruits)}."    
print(fruit_list)
# Example of using f-strings with functions
def greet(name):
    return f"Hello, {name}!"
print(greet("Bob"))
# Example of using f-strings with mathematical expressions
a = 5
b = 3
sum_result = f"The sum of {a} and {b} is {a + b}."
print(sum_result)
# Example of using f-strings with conditional expressions
is_adult = True
adult_status = f"I am {'an adult' if is_adult else 'a minor'}."
print(adult_status)


# Example of using f-strings with objects
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"My name is {self.name} and I am {self.age} years old." 
person = Person("Charlie", 35)
print(f"{person}")  # Implicitly calls the __str__ method

# Example of using f-strings with lists and loops
numbers = [1, 2, 3, 4, 5]
squared_numbers = [f"{num} squared is {num ** 2}" for num in numbers]
print("\n".join(squared_numbers))

# Example of using f-strings with list comprehensions
squared_numbers = [f"{num} squared is {num ** 2}" for num in range(1, 6)]
print(squared_numbers)

# Example of using f-strings with dictionaries and loops
people = {"Alice": 30, "Bob": 25, "Charlie": 35}
people_info = [f"{name} is {age} years old." for name, age in people.items()]
print("\n".join(people_info))



# Example of using f-strings with multi-line strings
multi_line = f"""This is a multi-line string.
It can span multiple lines.
And you can use f-strings inside it as well."""
print(multi_line)



# Example of using f-strings with formatting options
number = 123.456789
formatted_number = f"The number is: {number:.2f}"  # Format to 2 decimal places
print(formatted_number)


# Example of using f-strings with nested expressions
nested = f"The result of {x} * {y} is {x * y}, and the square of that is {(x * y) ** 2}."
print(nested)


# Example of using f-strings with conditional expressions   
is_even = True
conditional = f"The number is {'even' if is_even else 'odd'}."
print(conditional)



# Example of using f-strings with date formatting
from datetime import datetime
current_date = datetime.now()
formatted_date = f"Today's date is: {current_date:%Y-%m-%d %H:%M:%S}"  # Format date and time
print(formatted_date)

# Example of using f-strings with escape characters
escaped = f"This is a string with a newline character.\nAnd this is the second line."
print(escaped)
from datetime import datetime
current_date = datetime.now()
formatted_date = f"Today's date is: {current_date:%Y-%m-%d %H:%M:%S}"  # Format date and time   
print(formatted_date)



