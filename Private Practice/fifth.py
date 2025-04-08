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
