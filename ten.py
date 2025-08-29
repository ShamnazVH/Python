#exception examples
'''
zeroDivisionError ,ValueError
try:
    a = int(input("Enter numerator: "))
    b = int(input("Enter denominator: "))
    result = a / b
    print("Result:", result)
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")
except ValueError:#when character is entered
    print("Error: Please enter valid integers.")'''

#InderError
'''my_list = [10, 20, 30, 40]

try:
    idx = int(input("Enter an index: "))
    print("Element:", my_list[idx])
except IndexError:
    print("Error: Index out of range.")
except ValueError:
    print("Error: Invalid input. Please enter a number.")
'''





'''class CustomError(Exception):
    pass

try:
    user_input = int(input("Enter a number under 50: "))
    if user_input >= 50:
        raise CustomError("Number is too large.")
    print("You entered:", user_input)
except CustomError as e:
    print("Custom Error:", e)
finally:
    print("Execution completed.")'''

# try:
#     filename = "log.txt"
#     f = open(filename, "a")
#     raise ValueError("Simulated write error")  # simulate error (optional)
# except ValueError as e:
#     print("A value error occurred:", e)
# else:
#     f.write("New log entry\n")
#     f.close()
# finally:
#     print(f"Operation attempted on file: {filename}")


# Phone Number Formatter
# Given a string with phone numbers in various formats
#  (e.g., 1234567890, (123) 456-7890), use regex to 
# extract and reformat all into +91-123-456-7890.



#ary of categories with corresponding numbers.
#  Categorize Numbers
# Given a list of integers, categorize them into:
# Even numbers
# Odd numbers
# Prime numbers
# Multiples of 5
# Return a diction
# n = int(input("enter the elements to be inserted into list:"))
# my_list = []
# for i in range(n):
#     item = input(f"items to be inserted{i + 1}:")
#     item.append(my_list)
    
# for i in range(n):
#     if n % 2 == 0:
#         print("even")
#     else:
#        print("odd")
    
# Text Compression (Remove Repeated Characters)
# Input: "heee llooooo"
# Output: "helo"
# Use a loop to compress consecutive repeating characters.
# import re
# text = "heee llooooo"
# y =re.sub(r'(.)\1+','r\1',text)
# print(y)


# def is_prime(num):
#     if num <= 1:
#         return False
#     for i in range(2, int(num**0.5)+1):
#         if num % i == 0:
#             return False
#     return True

# n = int(input("Enter how many elements to insert into the list: "))
# my_list = []

# for i in range(n):
#     item = int(input(f"Enter item {i + 1}: "))
#     my_list.append(item)

# categories = {
#     "Even Numbers": [],
#     "Odd Numbers": [],
#     "Prime Numbers": [],
#     "Multiples of 5": []
# }

# for num in my_list:
#     if num % 2 == 0:
#         categories["Even Numbers"].append(num)
#     else:
#         categories["Odd Numbers"].append(num)

#     if is_prime(num):
#         categories["Prime Numbers"].append(num)

#     if num % 5 == 0:
#         categories["Multiples of 5"].append(num)

# print("\nCategorized Numbers:")
# for key, value in categories.items():
#     print(f"{key}: {value}")








    def is_