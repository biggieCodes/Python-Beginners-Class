#strings processing
# # The range is displayed to the user before taking input. 
# # The input() function can also take a generator expression as an argument.       
# # The generator expression is displayed to the user before taking input.


#example of a list with a list comprehension
my_comp_list = [x for x in range(1, 6)] 
print(my_comp_list) #Output: [1, 2, 3, 4, 5]

#example of a list with a generator expression
my_gen_list = list(x for x in range(1, 6))
print(my_gen_list) #Output: [1, 2, 3, 4, 5]

#example of a list with a lambda function
my_lambda_list = list(map(lambda x: x * 2, range(1, 6)))
print(my_lambda_list) #Output: [2, 4, 6, 8, 10]

#example of a list with a filter function
my_filter_list = list(filter(lambda x: x % 2 == 0, range(1, 11)))
print(my_filter_list) #Output: [2, 4, 6, 8, 10]
#

