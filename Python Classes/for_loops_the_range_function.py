#write a code that loops through a range of numbers from 1 -100 and does the following:
#1. prints the number if it is divisible by 3, the code should return "Fizz"
#2. prints the number if it is divisible by 5, the code should return "Buzz"
#3. prints the number if it is divisible by both 3 and 5, the code should return "FizzBuzz"


for number in range(1, 101): 
    
# Loop through numbers from 1 to 100

    if number % 3 == 0 and number % 5 == 0:  
# Check if divisible by both 3 and 5
        print(number, "FizzBuzz")
    elif number % 3 == 0:  
# Check if divisible by 3
        print(number,"Fizz")
    elif number % 5 == 0:  
# Check if divisible by 5
        print(number, "Buzz")
    else:
        print(number)  
# Print the number if none of the above conditions are met


# print the number of the letters in the word "Biggie" without using the len function

name = "Biggie"
count = 0
for letter in name:
    count += 1
print("The number of letters in the word 'Biggie' is:", count)  











