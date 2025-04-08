# type

x = 3
y = 5.0
z = 3e2

type_x = type(type_x)
print(type_x)

print(type(x + y / z))

# #Example of a list with a map function
# my_map_list = list(map(lambda x: x * 2, range(1, 6)))
# print(my_map_list) #Output: [2, 4, 6, 8, 10] = type(x)

# #Example of a list with a filter function
# my_filter_list = list(filter(lambda x: x % 2 == 0, range(1, 11)))
# print(my_filter_list) #Output: [2, 4, 6, 8, 10]

# #Example of a list with a reduce function
from functools import reduce
my_reduce_list = reduce(lambda x, y: x + y, range(1, 6))
print(my_reduce_list) #Output: 15

# #Example of a list with a zip function
my_zip_list = list(zip(range(1, 6), range(6, 11)))
print(my_zip_list) #Output: [(1, 6), (2, 7), (3, 8), (4, 9), (5, 10)]

# #Example of a list with a map function
my_map_list = list(map(lambda x: x * 2, range(1, 6)))
print(my_map_list) #Output: [2, 4, 6, 8, 10]
#


#Example of a list with a filter function
my_filter_list = list(filter(lambda x: x % 2 == 0, range(1, 11)))
print(my_filter_list) #Output: [2, 4, 6, 8, 10]

# #Example of a list with a reduce function
from functools import reduce
my_reduce_list = reduce(lambda x, y: x + y, range(1, 6))
print(my_reduce_list) #Output: 15


 
