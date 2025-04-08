#Lists
#what is a list?
#A list is a collection of items in a particular order.
#Lists are mutable, meaning they can be changed.
#Lists are defined using square brackets [].    
#Lists can contain any data type, including other lists.
#Lists can be nested, meaning a list can contain other lists.
#Lists can be empty, meaning they can contain no items.
#Lists can be indexed, meaning you can access individual items using their index.
#Lists can be sliced, meaning you can access a range of items using their index.
#Lists can be iterated, meaning you can loop through the items in a list.
#Lists can be sorted, meaning you can arrange the items in a particular order.
#Lists can be reversed, meaning you can reverse the order of the items in a list.
#Lists can be concatenated, meaning you can combine two or more lists into one.
#Lists can be repeated, meaning you can repeat the items in a list a certain number of times.
#Lists can be copied, meaning you can create a new list that is a copy of an existing list.
#Lists can be cleared, meaning you can remove all items from a list.
#Lists can be extended, meaning you can add items from one list to another.
#Lists can be inserted, meaning you can add an item at a specific index in a list.
#Lists can be removed, meaning you can remove an item from a list.
#Lists can be counted, meaning you can count the number of times an item appears in a list.


#Example of a list
my_list = [1, 2, 3, 4, 5]
print(my_list) #Output: [1, 2, 3, 4, 5]

#Example of a nested list
my_nested_list = [1, 2, [3, 4], 5]
print(my_nested_list) #Output: [1, 2, [3, 4], 5]

#Example of an empty list       
my_empty_list = []
print(my_empty_list) #Output: []

#Example of a list with different data types
my_mixed_list = [1, "two", 3.0, True]
print(my_mixed_list) #Output: [1, "two", 3.0, True]

#Example of a list with a string
my_string_list = ["apple", "banana", "cherry"]
print(my_string_list) #Output: ["apple", "banana", "cherry"]

#Example of a list with a tuple
my_tuple_list = [(1, 2), (3, 4), (5, 6)]
print(my_tuple_list) #Output: [(1, 2), (3, 4), (5, 6)]

#Example of a list with a dictionary
my_dict_list = [{"name": "Alice"}, {"name": "Bob"}, {"name": "Charlie"}]
print(my_dict_list) #Output: [{"name": "Alice"}, {"name": "Bob"}, {"name": "Charlie"}]

#Example of a list with a set
my_set_list = [{1, 2}, {3, 4}, {5, 6}]
print(my_set_list) #Output: [{1, 2}, {3, 4}, {5, 6}]

#Example of a list with a boolean
my_bool_list = [True, False, True]
print(my_bool_list) #Output: [True, False, True]

#Example of a list with a float
my_float_list = [1.0, 2.0, 3.0]
print(my_float_list) #Output: [1.0, 2.0, 3.0]

#Example of a list with a complex number
my_complex_list = [1 + 2j, 3 + 4j, 5 + 6j]
print(my_complex_list) #Output: [(1+2j), (3+4j), (5+6j)]


#Example of a list with a range
my_range_list = list(range(1, 6))
print(my_range_list) #Output: [1, 2, 3, 4, 5]

#Example of a list with a list comprehension
my_comp_list = [x for x in range(1, 6)]
print(my_comp_list) #Output: [1, 2, 3, 4, 5]

#Example of a list with a generator expression
my_gen_list = list(x for x in range(1, 6))
print(my_gen_list) #Output: [1, 2, 3, 4, 5]

#Example of a list with a lambda function
my_lambda_list = list(map(lambda x: x * 2, range(1, 6)))
print(my_lambda_list) #Output: [2, 4, 6, 8, 10]

#Example of a list with a filter function
my_filter_list = list(filter(lambda x: x % 2 == 0, range(1, 11)))
print(my_filter_list) #Output: [2, 4, 6, 8, 10]

#Example of a list with a reduce function
from functools import reduce
my_reduce_list = reduce(lambda x, y: x + y, range(1, 6))
print(my_reduce_list) #Output: 15

#Example of a list with a zip function
my_zip_list = list(zip(range(1, 6), range(6, 11)))
print(my_zip_list) #Output: [(1, 6), (2, 7), (3, 8), (4, 9), (5, 10)]


#Example of a list with a map function
my_map_list = list(map(lambda x: x * 2, range(1, 6)))
print(my_map_list) #Output: [2, 4, 6, 8, 10]

#Example of a list with a filter function
my_filter_list = list(filter(lambda x: x % 2 == 0, range(1, 11)))
print(my_filter_list) #Output: [2, 4, 6, 8, 10]

#Example of a list with a reduce function
from functools import reduce
my_reduce_list = reduce(lambda x, y: x + y, range(1, 6))
print(my_reduce_list) #Output: 15

#Example of a list with a zip function
my_zip_list = list(zip(range(1, 6), range(6, 11)))
print(my_zip_list) #Output: [(1, 6), (2, 7), (3, 8), (4, 9), (5, 10)]


#Example of a list with a map function
my_map_list = list(map(lambda x: x * 2, range(1, 6)))
print(my_map_list) #Output: [2, 4, 6, 8, 10]


#Example of a list with a filter function
my_filter_list = list(filter(lambda x: x % 2 == 0, range(1, 11)))
print(my_filter_list) #Output: [2, 4, 6, 8, 10]

#tuple
#A tuple is a collection of items in a particular order.
#Tuples are immutable, meaning they cannot be changed.
#Tuples are defined using parentheses ().
#Tuples can contain any data type, including other tuples.
#Tuples can be nested, meaning a tuple can contain other tuples.
#Tuples can be empty, meaning they can contain no items.
#Tuples can be indexed, meaning you can access individual items using their index.
#Tuples can be sliced, meaning you can access a range of items using their index.
#Tuples can be iterated, meaning you can loop through the items in a tuple.
#Tuples can be sorted, meaning you can arrange the items in a particular order.
#Tuples can be reversed, meaning you can reverse the order of the items in a tuple.
#Tuples can be concatenated, meaning you can combine two or more tuples into one.
#Tuples can be repeated, meaning you can repeat the items in a tuple a certain number of times.
#Tuples can be copied, meaning you can create a new tuple that is a copy of an existing tuple.
#Tuples can be cleared, meaning you can remove all items from a tuple.
#Tuples can be extended, meaning you can add items from one tuple to another.
#Tuples can be inserted, meaning you can add an item at a specific index in a tuple.
#Tuples can be removed, meaning you can remove an item from a tuple.
#Tuples can be counted, meaning you can count the number of times an item appears in a tuple.


#Example of a tuple
my_tuple = (1, 2, 3, 4, 5)
print(my_tuple) #Output: (1, 2, 3, 4, 5)

#Example of a nested tuple
my_nested_tuple = (1, 2, (3, 4), 5)
print(my_nested_tuple) #Output: (1, 2, (3, 4), 5)

#Example of an empty tuple
my_empty_tuple = ()
print(my_empty_tuple) #Output: ()

#Example of a tuple with different data types
my_mixed_tuple = (1, "two", 3.0, True)
print(my_mixed_tuple) #Output: (1, "two", 3.0, True)

#Example of a tuple with a string
my_string_tuple = ("apple", "banana", "cherry")
print(my_string_tuple) #Output: ("apple", "banana", "cherry")

#Example of a tuple with a list
my_list_tuple = ([1, 2], [3, 4], [5, 6])
print(my_list_tuple) #Output: ([1, 2], [3, 4], [5, 6])

#Example of a tuple with a dictionary
my_dict_tuple = ({"name": "Biggie"}, {"name": "Kizzy"}, {"name": "Songs"})
print(my_dict_tuple) #Output: ({"name": "Biggie"}, {"name": "Kizzy"}, {"name": "Songs"})

#Example of a tuple with a set
my_set_tuple = ({1, 2}, {3, 4}, {5, 6})
print(my_set_tuple) #Output: ({1, 2}, {3, 4}, {5, 6})

#Example of a tuple with a boolean
my_bool_tuple = (True, False, True)
print(my_bool_tuple) #Output: (True, False, True)

#Example of a tuple with a float
my_float_tuple = (1.0, 2.0, 3.0)
print(my_float_tuple) #Output: (1.0, 2.0, 3.0)

#Example of a tuple with a complex number
my_complex_tuple = (1 + 2j, 3 + 4j, 5 + 6j)
print(my_complex_tuple) #Output: ((1+2j), (3+4j), (5+6j))

#Example of a tuple with a range
my_range_tuple = tuple(range(1, 6))
print(my_range_tuple) #Output: (1, 2, 3, 4, 5)

#Example of a tuple with a tuple comprehension
my_comp_tuple = tuple(x for x in range(1, 6))
print(my_comp_tuple) #Output: (1, 2, 3, 4, 5)

#Example of a tuple with a generator expression
my_gen_tuple = tuple(x for x in range(1, 6))
print(my_gen_tuple) #Output: (1, 2, 3, 4, 5)

#Example of a tuple with a lambda function
my_lambda_tuple = tuple(map(lambda x: x * 2, range(1, 6)))
print(my_lambda_tuple) #Output: (2, 4, 6, 8, 10)

#Example of a tuple with a filter function
my_filter_tuple = tuple(filter(lambda x: x % 2 == 0, range(1, 11)))
print(my_filter_tuple) #Output: (2, 4, 6, 8, 10)

#Example of a tuple with a reduce function
from functools import reduce
my_reduce_tuple = reduce(lambda x, y: x + y, range(1, 6))
print(my_reduce_tuple) #Output: 15

#Example of a tuple with a zip function
my_zip_tuple = tuple(zip(range(1, 6), range(6, 11)))
print(my_zip_tuple) #Output: ((1, 6), (2, 7), (3, 8), (4, 9), (5, 10))

#Example of a tuple with a map function
my_map_tuple = tuple(map(lambda x: x * 2, range(1, 6)))
print(my_map_tuple) #Output: (2, 4, 6, 8, 10)

#Example of a tuple with a filter function
my_filter_tuple = tuple(filter(lambda x: x % 2 == 0, range(1, 11)))
print(my_filter_tuple) #Output: (2, 4, 6, 8, 10)

#Example of a tuple with a reduce function
from functools import reduce
my_reduce_tuple = reduce(lambda x, y: x + y, range(1, 6))
print(my_reduce_tuple) #Output: 15
















