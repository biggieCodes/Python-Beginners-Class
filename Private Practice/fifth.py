#f_strings


name = "Biggie"
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
person = {"name": "Biggie", "age": 30}
info = f"My name is {person['name']} and I am {person['age']} years old."   
print(info)


# Example of using f-strings with lists 
fruits = ["apple", "banana", "cherry"]
fruit_list = f"My favorite fruits are: {', '.join(fruits)}."    
print(fruit_list)

# Example of using f-strings with tuples
coordinates = (10, 20)
coordinate_string = f"The coordinates are: ({coordinates[0]}, {coordinates[1]})."
print(coordinate_string)

# Example of using f-strings with sets
unique_numbers = {1, 2, 3, 4, 5}
unique_numbers_string = f"The unique numbers are: {', '.join(map(str, unique_numbers))}."
print(unique_numbers_string)

# Example of using f-strings with booleans
is_active = True
status = f"The user is {'active' if is_active else 'inactive'}."
print(status)

# Example of using f-strings with None
is_none = None
none_status = f"The value is {'None' if is_none is None else 'not None'}."
print(none_status)

# Example of using f-strings with string methods
text = "Hello, World!"
uppercase_text = f"The uppercase version of the text is: {text.upper()}."
print(uppercase_text)

# Example of using f-strings with functions
def greet(name):
    return f"Hello, {name}!"
print(greet("Bob"))

# Example of using f-strings with string formatting
number = 123.456789
formatted_number = f"The formatted number is: {number:.2f}"  # Format to 2 decimal places
print(formatted_number)

# Example of using f-strings with string slicing
text = "Hello, World!"
sliced_text = f"The first 5 characters are: {text[:5]}."
print(sliced_text)

# Example of using f-strings with string concatenation
text1 = "Hello"
text2 = "World"
concatenated_text = f"{text1}, {text2}!"
print(concatenated_text)

# Example of using f-strings with string length
text = "Hello, World!"
length = f"The length of the text is: {len(text)} characters."
print(length)

# Example of using f-strings with string replacement
text = "Hello, {name}!"
name = "Biggie"
replaced_text = f"{text.replace('{name}', name)}"
print(replaced_text)

# Example of using f-strings with string formatting options
text = "Hello, {name}!"
name = "Biggie"
formatted_text = f"{text.format(name=name)}"
print(formatted_text)

# Example of using f-strings with string interpolation
text = "Hello, {name}!"
name = "Biggie"
interpolated_text = f"{text.format(name=name)}"
print(interpolated_text)

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
person = Person("Songs", 35)
print(f"{person}")  # Implicitly calls the __str__ method

# Example of using f-strings with lists and loops
numbers = [1, 2, 3, 4, 5]
squared_numbers = [f"{num} squared is {num ** 2}" for num in numbers]
print("\n".join(squared_numbers))


# Example of using f-strings with dictionaries and loops
people = {"Biggie": 30, "kizzy": 25, "Songs": 35}
people_info = [f"{name} is {age} years old." for name, age in people.items()]
print("\n".join(people_info))


# Example of using f-strings with sets and loops
unique_numbers = {1, 2, 3, 4, 5}
unique_numbers_string = [f"The unique number is: {num}" for num in unique_numbers]
print("\n".join(unique_numbers_string))


# Example of using f-strings with booleans
is_active = True
status = f"The user is {'active' if is_active else 'inactive'}."
print(status)

# Example of using f-strings with booleans and loops
is_active = [True, False, True]
status = [f"The user is {'active' if active else 'inactive'}." for active in is_active]
print("\n".join(status))

# Example of using f-strings with tuples and loops
coordinates = [(10, 20), (30, 40), (50, 60)]
coordinate_strings = [f"The coordinates are: ({x}, {y})." for x, y in coordinates]
print("\n".join(coordinate_strings))

# Example of using f-strings with string methods and loops
text_list = ["Hello", "World", "Python"]
uppercase_texts = [f"The uppercase version of the text is: {text.upper()}." for text in text_list]
print("\n".join(uppercase_texts))

# Example of using f-strings with string slicing and loops
text_list = ["Hello, World!", "Python is great!", "F-strings are awesome!"]
sliced_texts = [f"The first 5 characters are: {text[:5]}." for text in text_list]
print("\n".join(sliced_texts))

# Example of using f-strings with string concatenation and loops
text1_list = ["Hello", "Goodbye"]
text2_list = ["World", "Everyone"]
concatenated_texts = [f"{text1}, {text2}!" for text1, text2 in zip(text1_list, text2_list)]
print("\n".join(concatenated_texts))

# Example of using f-strings with string length and loops
text_list = ["Hello, World!", "Python is great!", "F-strings are awesome!"]
lengths = [f"The length of the text is: {len(text)} characters." for text in text_list]
print("\n".join(lengths))

# Example of using f-strings with string replacement and loops
text_list = ["Hello, {name}!", "Goodbye, {name}!"]
name_list = ["Biggie", "kizzy"]
replaced_texts = [f"{text.replace('{name}', name)}" for text, name in zip(text_list, name_list)]
print("\n".join(replaced_texts))

# Example of using f-strings with string formatting options and loops   
text_list = ["Hello, {name}!", "Goodbye, {name}!"]
name_list = ["Biggie", "kizzy"]
formatted_texts = [f"{text.format(name=name)}" for text, name in zip(text_list, name_list)]
print("\n".join(formatted_texts))

# Example of using f-strings with string interpolation and loops
text_list = ["Hello, {name}!", "Goodbye, {name}!"]
name_list = ["Biggie", "kizzy"]
interpolated_texts = [f"{text.format(name=name)}" for text, name in zip(text_list, name_list)]
print("\n".join(interpolated_texts))

# Example of using f-strings with mathematical expressions and loops
a_list = [5, 10, 15]
b_list = [3, 6, 9]
sum_results = [f"The sum of {a} and {b} is {a + b}." for a, b in zip(a_list, b_list)]
print("\n".join(sum_results))

# Example of using f-strings with conditional expressions and loops
is_adult_list = [True, False, True]
adult_statuses = [f"I am {'an adult' if is_adult else 'a minor'}." for is_adult in is_adult_list]
print("\n".join(adult_statuses))

# Example of using f-strings with objects and loops
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"My name is {self.name} and I am {self.age} years old."
people = [Person("Biggie", 30), Person("kizzy", 25), Person("Songs", 35)]
people_strings = [f"{person}" for person in people]
print("\n".join(people_strings))

# Example of using f-strings with functions and loops
def greet(name):
    return f"Hello, {name}!"
names = ["Biggie", "kizzy", "Songs"]
greetings = [greet(name) for name in names]
print("\n".join(greetings))  # Output: Hello, Biggie! Hello, kizzy! Hello, Songs!


# Example of using f-strings with functions
def greet(name):
    return f"Hello, {name}!"
print(greet("Biggie"))  # Output: Hello, Biggie!



# Example of using f-strings with functions and loops
def greet_multiple(names):
    return [f"Hello, {name}!" for name in names]
names = ["Biggie", "kizzy", "Songs"]
greetings = greet_multiple(names)
print("\n".join(greetings))  # Output: Hello, Biggie! Hello, kizzy! Hello, Songs!





# Example of using f-strings with loops
for i in range(5):
    print(f"Iteration {i + 1}: Hello, {name}!")
    



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

# Example of using f-strings with escape characters
escaped = f"This is a string with a newline character.\nAnd this is the second line."   
print(escaped)


# Example of using f-strings with special characters
special_characters = f"This string contains special characters: @#$%^&*()!"
print(special_characters)

# Example of using f-strings with Unicode characters
unicode_string = f"This string contains Unicode characters: 😊, 你好, Привет!"
print(unicode_string)

# Example of using f-strings with raw strings
raw_string = rf"This is a raw string: \n\tThis will not be escaped."
print(raw_string)

# Example of using f-strings with HTML
html_string = f"<html><body><h1>Hello, {name}!</h1></body></html>"
print(html_string)

# Example of using f-strings with JSON
import json
data = {"name": "Biggie", "age": 30}
json_string = f"JSON data: {json.dumps(data)}"
print(json_string)

# Example of using f-strings with XML
xml_string = f"<person><name>{name}</name><age>{age}</age></person>"
print(xml_string)

# Example of using f-strings with URL encoding
import urllib.parse
url = f"https://example.com/search?q={urllib.parse.quote('Hello World')}"
print(url)

# Example of using f-strings with Markdown
markdown_string = f"# Hello, {name}!\nThis is a Markdown string."
print(markdown_string)

# Example of using f-strings with CSV
import csv

data = [["name", "age"], ["Alice", 30], ["Bob", 25]]
csv_string = f"CSV data:\n{''.join([','.join(map(str, row)) + '\n' for row in data])}"
print(csv_string)





